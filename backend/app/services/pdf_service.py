"""PDF report generation service."""
import os
from io import BytesIO
from datetime import datetime
from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)

try:
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image, PageBreak
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
    HAS_REPORTLAB = True
except ImportError:
    HAS_REPORTLAB = False
    logger.warning("reportlab not installed. PDF generation will be limited.")


def generate_prediction_report_pdf(
    prediction_data: Dict[str, Any],
    patient_info: Optional[Dict[str, Any]] = None,
    output_path: Optional[str] = None
) -> Optional[bytes]:
    """
    Generate PDF report for a prediction.
    
    Args:
        prediction_data: Dictionary containing prediction results
        patient_info: Optional patient demographic information
        output_path: Optional file path to save PDF (if not provided, returns bytes)
    
    Returns:
        PDF as bytes if output_path not provided, else None
    """
    if not HAS_REPORTLAB:
        logger.error("reportlab not installed. Cannot generate PDF.")
        return None
    
    try:
        # Create PDF document
        pdf_buffer = BytesIO()
        doc = SimpleDocTemplate(
            pdf_buffer,
            pagesize=letter,
            rightMargin=0.5*inch,
            leftMargin=0.5*inch,
            topMargin=0.5*inch,
            bottomMargin=0.5*inch
        )
        
        # Container for PDF elements
        elements = []
        
        # Define styles
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#003366'),
            spaceAfter=12,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        )
        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=14,
            textColor=colors.HexColor('#006699'),
            spaceAfter=8,
            spaceBefore=12,
            fontName='Helvetica-Bold'
        )
        normal_style = styles['Normal']
        
        # Title
        elements.append(Paragraph("Diabetic Foot Ulcer Analysis Report", title_style))
        elements.append(Spacer(1, 0.2*inch))
        
        # Report info
        report_date = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        elements.append(Paragraph(f"Report Generated: {report_date}", normal_style))
        elements.append(Spacer(1, 0.15*inch))
        
        # Patient information
        if patient_info:
            elements.append(Paragraph("Patient Information", heading_style))
            patient_data = [
                ["Field", "Value"],
                ["Patient ID", str(patient_info.get('patient_id', 'N/A'))],
                ["Age", str(patient_info.get('age', 'N/A'))],
                ["BMI", f"{patient_info.get('bmi', 'N/A')}"],
                ["Diabetes Duration", f"{patient_info.get('diabetes_duration', 'N/A')} years"],
                ["Infection Signs", str(patient_info.get('infection_signs', 'None')).title()]
            ]
            patient_table = Table(patient_data, colWidths=[2*inch, 3*inch])
            patient_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#006699')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            elements.append(patient_table)
            elements.append(Spacer(1, 0.2*inch))
        
        # Prediction Results
        elements.append(Paragraph("Analysis Results", heading_style))
        
        prediction = prediction_data.get('prediction', 'Unknown')
        confidence = prediction_data.get('confidence', 0.0)
        risk_score = prediction_data.get('risk_score', 0.0)
        risk_level = prediction_data.get('risk_level', 'Unknown')
        severity = prediction_data.get('severity', 'Unknown')
        affected_area = prediction_data.get('affected_area', 0.0)
        
        results_data = [
            ["Metric", "Result"],
            ["Prediction", prediction.upper()],
            ["Confidence", f"{confidence*100:.1f}%"],
            ["Risk Score", f"{risk_score:.1f}/100"],
            ["Risk Level", risk_level],
            ["Severity", severity],
            ["Affected Area", f"{affected_area:.1f}%"]
        ]
        
        results_table = Table(results_data, colWidths=[2*inch, 3*inch])
        results_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#006699')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.lightblue),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        elements.append(results_table)
        elements.append(Spacer(1, 0.2*inch))
        
        # Clinical Explanation
        elements.append(Paragraph("Clinical Analysis", heading_style))
        explanation = prediction_data.get('explanation_text', 'No explanation available')
        elements.append(Paragraph(explanation, normal_style))
        elements.append(Spacer(1, 0.15*inch))
        
        # LIME Analysis
        lime_explanation = prediction_data.get('lime_explanation', '')
        if lime_explanation:
            elements.append(Paragraph("LIME Explanation", heading_style))
            elements.append(Paragraph(lime_explanation, normal_style))
            elements.append(Spacer(1, 0.15*inch))
        
        # Recommendations
        recommendations = prediction_data.get('recommendations', [])
        if recommendations:
            elements.append(Paragraph("Clinical Recommendations", heading_style))
            rec_text = "<br/>".join([f"• {rec}" for rec in recommendations])
            elements.append(Paragraph(rec_text, normal_style))
            elements.append(Spacer(1, 0.15*inch))
        
        # Feature Importance
        shap_importance = prediction_data.get('shap_importance', {})
        if shap_importance:
            elements.append(Paragraph("Feature Importance (SHAP)", heading_style))
            shap_data = [["Feature", "Importance"]]
            for feat, importance in sorted(shap_importance.items(), 
                                          key=lambda x: x[1], reverse=True):
                shap_data.append([feat, f"{importance:.3f}"])
            
            shap_table = Table(shap_data, colWidths=[2*inch, 3*inch])
            shap_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#006699')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 11),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
                ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            elements.append(shap_table)
        
        elements.append(Spacer(1, 0.3*inch))
        
        # Footer
        footer_text = "This report was automatically generated by MedVision AI. Please review with qualified medical professionals."
        elements.append(Paragraph(footer_text, normal_style))
        
        # Build PDF
        doc.build(elements)
        pdf_buffer.seek(0)
        
        # Save to file if path provided
        if output_path:
            with open(output_path, 'wb') as f:
                f.write(pdf_buffer.getvalue())
            logger.info(f"PDF report saved to {output_path}")
            return None
        
        return pdf_buffer.getvalue()
    
    except Exception as e:
        logger.error(f"Error generating PDF: {str(e)}")
        return None


def generate_patient_analysis_pdf(
    patient_id: int,
    patient_name: str,
    analyses: list,
    output_path: Optional[str] = None
) -> Optional[bytes]:
    """
    Generate comprehensive PDF report for multiple analyses of a patient.
    
    Args:
        patient_id: Patient identifier
        patient_name: Patient name or identifier
        analyses: List of analysis dictionaries
        output_path: Optional file path to save PDF
    
    Returns:
        PDF as bytes or None if saved to file
    """
    if not HAS_REPORTLAB:
        logger.error("reportlab not installed. Cannot generate PDF.")
        return None
    
    try:
        pdf_buffer = BytesIO()
        doc = SimpleDocTemplate(
            pdf_buffer,
            pagesize=A4,
            rightMargin=0.5*inch,
            leftMargin=0.5*inch,
            topMargin=0.5*inch,
            bottomMargin=0.5*inch
        )
        
        elements = []
        styles = getSampleStyleSheet()
        
        # Title
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=22,
            textColor=colors.HexColor('#003366'),
            spaceAfter=12,
            alignment=TA_CENTER
        )
        elements.append(Paragraph("Patient Analysis History", title_style))
        elements.append(Paragraph(f"Patient: {patient_name} (ID: {patient_id})", styles['Normal']))
        elements.append(Paragraph(f"Report Date: {datetime.utcnow().strftime('%Y-%m-%d')}", styles['Normal']))
        elements.append(Spacer(1, 0.3*inch))
        
        # Summary table
        summary_data = [["Date", "Prediction", "Confidence", "Risk Level", "Notes"]]
        for analysis in analyses:
            date_str = analysis.get('timestamp', 'N/A')[:10]
            summary_data.append([
                date_str,
                analysis.get('prediction', 'N/A').upper(),
                f"{analysis.get('confidence', 0)*100:.1f}%",
                analysis.get('risk_level', 'N/A'),
                ""
            ])
        
        summary_table = Table(summary_data, colWidths=[1.2*inch, 1.2*inch, 1.2*inch, 1.2*inch, 1.2*inch])
        summary_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#006699')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        elements.append(summary_table)
        
        # Build PDF
        doc.build(elements)
        pdf_buffer.seek(0)
        
        if output_path:
            with open(output_path, 'wb') as f:
                f.write(pdf_buffer.getvalue())
            logger.info(f"Patient analysis PDF saved to {output_path}")
            return None
        
        return pdf_buffer.getvalue()
    
    except Exception as e:
        logger.error(f"Error generating patient analysis PDF: {str(e)}")
        return None
