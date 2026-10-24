from lead_enricher.cli import main
from lead_enricher.enricher import enrich_domain


def test_enrich_known_domain():
    lead = enrich_domain("https://stripe.com/pricing")
    assert lead.domain == "stripe.com"
    assert lead.company_name == "Stripe, Inc."
    assert "Fintech" in lead.industry
    assert lead.fit_score >= 8
    assert len(lead.tech_stack) > 0


def test_enrich_unknown_fallback():
    lead = enrich_domain("unknownstartup123.io")
    assert lead.domain == "unknownstartup123.io"
    assert lead.company_name == "Unknownstartup123"
    assert lead.contact_email == "contact@unknownstartup123.io"
    assert lead.fit_score == 5


def test_cli_execution(capsys):
    exit_code = main(["stripe.com"])
    assert exit_code == 0
    captured = capsys.readouterr()
    assert "LEAD ENRICHER PRO" in captured.out
    assert "Stripe, Inc." in captured.out
    assert "Fit Score" in captured.out
