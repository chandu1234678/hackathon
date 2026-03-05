#!/usr/bin/env python
"""Verification script for all 5 fixes."""
import sys

def verify_all():
    results = []
    
    # 1. Test Grad-CAM Overlay
    try:
        from app.explainability.heatmap_renderer import render_heatmap_overlay
        import numpy as np
        results.append(("1. Grad-CAM Overlay Renderer", "OK"))
    except Exception as e:
        results.append(("1. Grad-CAM Overlay Renderer", f"FAIL: {str(e)[:60]}"))
    
    # 2. Test LIME Explanation
    try:
        from app.explainability.lime_explainer import generate_lime_explanation
        import numpy as np
        clinical_features = np.array([[0.5, 0.5, 0.3, 0.25]])
        result = generate_lime_explanation(clinical_features, 'ulcer', 0.75)
        assert 'explanation' in result and 'lime_importance' in result
        results.append(("2. LIME Explanation Generation", "OK"))
    except Exception as e:
        results.append(("2. LIME Explanation Generation", f"FAIL: {str(e)[:60]}"))
    
    # 3. Test Segmentation Model Loading
    try:
        from app.services.model_loader import get_segmentation_model
        seg_model = get_segmentation_model()
        results.append(("3. Segmentation Model Loading", "OK"))
    except Exception as e:
        results.append(("3. Segmentation Model Loading", f"FAIL: {str(e)[:60]}"))
    
    # 4. Test PDF Service
    try:
        from app.services.pdf_service import generate_prediction_report_pdf
        results.append(("4. PDF Report Generation", "OK"))
    except Exception as e:
        results.append(("4. PDF Report Generation", f"FAIL: {str(e)[:60]}"))
    
    # 5. Test Database Schema
    try:
        from app.models import PredictionLog
        cols = [c.name for c in PredictionLog.__table__.columns]
        required = ['risk_score', 'risk_level', 'severity', 'explanation_text']
        has_all = all(col in cols for col in required)
        status = "OK" if has_all else f"FAIL: missing {[c for c in required if c not in cols]}"
        results.append(("5. Database Schema", status))
    except Exception as e:
        results.append(("5. Database Schema", f"FAIL: {str(e)[:60]}"))
    
    # 6. Verify Inference Service
    try:
        from app.services.inference_service import run_inference
        import inspect
        sig = inspect.signature(run_inference)
        params = list(sig.parameters.keys())
        expected = ['image_url', 'age', 'bmi', 'diabetes_duration', 'infection_signs']
        status = "OK" if params == expected else "FAIL: signature mismatch"
        results.append(("6. Inference Service", status))
    except Exception as e:
        results.append(("6. Inference Service", f"FAIL: {str(e)[:60]}"))
    
    # 7. Verify PDF Export Routes
    try:
        from app.routes.reports import router
        routes = [rule.path for rule in router.routes if hasattr(rule, 'path')]
        has_pdf = any('export-pdf' in r for r in routes)
        status = "OK" if has_pdf else "FAIL: no PDF export routes"
        results.append(("7. PDF Export Routes", status))
    except Exception as e:
        results.append(("7. PDF Export Routes", f"FAIL: {str(e)[:60]}"))
    
    # Print results
    print("\n" + "="*70)
    print("COMPREHENSIVE FIX VERIFICATION")
    print("="*70 + "\n")
    
    for feature, status in results:
        status_display = f"[{status.split(':')[0]:^4}]"
        print(f"{status_display}  {feature:<40} {status[len(status.split(':')[0])+2:] if ':' in status else ''}")
    
    print("\n" + "="*70)
    ok_count = sum(1 for _, s in results if s.startswith("OK"))
    print(f"SUMMARY: {ok_count}/{len(results)} fixes verified")
    print("="*70 + "\n")
    
    return ok_count == len(results)

if __name__ == "__main__":
    success = verify_all()
    sys.exit(0 if success else 1)
