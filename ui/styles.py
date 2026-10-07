def load_css() -> str:
    """
    Returns custom modern SaaS styling for the Streamlit application.
    """
    return """
    <style>
    /* Google Font Import */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        color: #1f2937;
    }

    /* Main Container Padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    /* Executive Hero Header */
    .hero-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 24px 32px;
        border-radius: 12px;
        color: #ffffff;
        margin-bottom: 24px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    }
    .hero-header h1 {
        color: #ffffff !important;
        font-size: 24px;
        font-weight: 700;
        margin: 0 0 6px 0;
    }
    .hero-header p {
        color: #94a3b8;
        font-size: 14px;
        margin: 0;
    }

    /* Modern Card UI */
    .metric-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 18px 22px;
        margin-bottom: 16px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.06);
    }
    .metric-card h4 {
        margin: 0 0 8px 0;
        color: #64748b;
        font-size: 13px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.6px;
    }
    .metric-card .metric-value {
        font-size: 28px;
        font-weight: 700;
        color: #0f172a;
    }

    /* Skill Badges Styling */
    .skill-badge {
        display: inline-block;
        background-color: #f1f5f9;
        color: #334155;
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 500;
        margin: 3px 5px 3px 0;
        border: 1px solid #cbd5e1;
    }
    .skill-badge-matched {
        background-color: #f0fdf4;
        color: #15803d;
        border: 1px solid #bbf7d0;
    }
    .skill-badge-missing {
        background-color: #fef2f2;
        color: #b91c1c;
        border: 1px solid #fecaca;
    }

    /* Feedback Callouts */
    .feedback-good {
        color: #15803d;
        font-weight: 500;
    }
    .feedback-warn {
        color: #b45309;
        font-weight: 500;
    }

    /* Clean Sidebar Override */
    section[data-testid="stSidebar"] {
        background-color: #f8fafc;
        border-right: 1px solid #e2e8f0;
    }

    /* Hide standard Streamlit header and footer branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """