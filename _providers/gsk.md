---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 27
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gsk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gsk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gsk.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GSK-Biostatistics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gsk
- group: other
  title: ''
  type: X
  url: https://x.com/GSK
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/GSKvision
- group: company
  title: ''
  type: Blog
  url: https://www.gsk.com/en-gb/behind-the-science-magazine/
- group: company
  title: ''
  type: Newsletter
  url: https://feed.podbean.com/behindthescience/feed.xml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.gsk.com/en-gb/media/press-releases/
- group: start
  title: ''
  type: ClinicalTrials
  url: https://www.gsk-studyregister.com/en/
- group: other
  title: ''
  type: DataSharing
  url: https://www.clinicalstudydatarequest.com
- group: other
  title: ''
  type: Transparency
  url: https://www.gsk.com/en-gb/innovation/trials/data-transparency/
- group: company
  title: ''
  type: Partners
  url: https://www.gsk.com/en-gb/innovation/partnerships/
- group: other
  title: ''
  type: Suppliers
  url: https://supplier.gsk.com
- group: other
  title: ''
  type: Customers
  url: https://www.gskpro.com
- group: company
  title: ''
  type: Investors
  url: https://www.gsk.com/en-gb/investors/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.gsk.com/en-gb/responsibility/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gsk.com/en-gb/privacy-notice/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gsk.com/en-gb/terms-of-use/
- group: operate
  title: ''
  type: Contact
  url: https://www.gsk.com/en-gb/contact-us/
- group: operate
  title: ''
  type: Support
  url: https://www.gsk.com/speakup
- group: other
  title: ''
  type: Resources
  url: https://www.gsk.com/en-gb/media/rss-feeds/
- group: auth
  title: ''
  type: Compliance
  url: ''
- group: build
  title: ''
  type: GitHubRepository
  url: ''
created: '2026-05-23'
description: GSK plc (formerly GlaxoSmithKline, rebranded in May 2022) is a global biopharma headquartered in the United Kingdom and dual-listed on the London Stock Exchange and NYSE under the ticker GSK. Following the July 2022 spin-off of its consumer-health business as Haleon, GSK is now a focused biopharma operating across four therapeutic areas — infectious diseases, HIV, oncology, and respiratory/immunology/inflammation — with flagship vaccine franchises including Shingrix and Arexvy and an HIV joint venture (ViiV Healthcare) held with Pfizer and Shionogi. GSK does not publish a public developer portal or commercial REST APIs. Machine-readable surfaces are limited to press, podcast and investor RSS feeds, the GSK Study Register and the ClinicalStudyDataRequest (CSDR) consortium portal for patient-level clinical trial data, registrations on ClinicalTrials.gov, and R/Python tooling published by the GSK-Biostatistics GitHub organization.
features:
- description: Public web register disclosing protocol summaries and results for GSK-sponsored clinical trials. Over 7,400 protocol summaries and 6,500 results summaries published since the register launched in 2004; search-only, no documented API.
  name: GSK Study Register
- description: GSK is a founding sponsor of ClinicalStudyDataRequest.com (CSDR), a 13-sponsor consortium portal where qualified researchers can request anonymized patient-level clinical study data subject to Independent Review Panel approval and a Data Sharing Agreement.
  name: Patient-Level Clinical Data Sharing
- description: More than 2,700 redacted Clinical Study Reports (CSRs) for approved GSK medicines and vaccines published since 2000, available through the Study Register and CSDR.
  name: Clinical Study Reports
- description: All GSK-sponsored interventional studies are registered and result-reported on ClinicalTrials.gov, the US federal registry, which itself offers a public REST API for third-party integration.
  name: ClinicalTrials.gov Registration
- description: Separate HIV-focused trial register operated by GSK's ViiV Healthcare joint venture at viiv-studyregister.com.
  name: ViiV Healthcare Study Register
- description: Five RSS feeds covering press releases, Behind the Science magazine, Behind the Science podcast, RNS stock-exchange announcements, and SEC filings (CIK 0001131399).
  name: Press & Investor RSS
- description: 29 public repositories of R and Python statistical tooling for clinical reporting (tfrmt, gto, slushy, beastt, cicalc) and CDISC clinical-data handling on Neo4j (neo4cdisc, neointerface, tab2neo).
  name: GSK Biostatistics Open Source
- description: gskpro.com provides authenticated HCPs with prescribing information, medical information requests, and product safety materials by country.
  name: Healthcare Professional Portal
- description: supplier.gsk.com gateway for registered suppliers covering invoice status, bank-detail management, and procurement onboarding.
  name: Supplier Portal
- description: Drug ordering, returns, chargebacks, and shipment notifications are exchanged with US distributors via X12 EDI rather than a public API.
  name: Distributor & Wholesaler EDI
- description: Adverse-event reports follow ICH E2B(R3) and are routed to regulators (FDA FAERS, EudraVigilance) rather than a public ingest API.
  name: Pharmacovigilance Reporting
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gsk.png
integrations:
- description: 13-sponsor consortium portal (Astellas, Bayer, Boehringer Ingelheim, Daiichi Sankyo, Eisai, GSK, Lilly, Novartis, Roche, Sanofi, Takeda, UCB, ViiV) for patient-level clinical trial data sharing.
  name: ClinicalStudyDataRequest.com (CSDR)
- description: US federal clinical trial registry where all GSK-sponsored interventional studies are registered and result-reported.
  name: ClinicalTrials.gov
- description: European registry (EU CTR / CTIS) for GSK trials conducted in EU/EEA.
  name: EU Clinical Trials Register
- description: Industry-wide platform for lay-language clinical trial result summaries.
  name: trialsummaries.com
- description: HIV-focused joint venture owned by GSK (majority), Pfizer, and Shionogi; operates its own trial register and product portfolio.
  name: ViiV Healthcare
- description: Consumer healthcare company spun off from GSK in July 2022; no longer part of GSK plc.
  name: Haleon
layout: provider
modified: '2026-05-23'
name: GSK
nav: Providers
network: true
overview: 'GSK is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Pharmaceuticals, Biotechnology, Vaccines, HIV, and Oncology.


  GSK''s developer surface includes YouTube channel, engineering blog, changelog, support, and 19 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 18.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gsk/refs/heads/main/screenshots/gsk-2026-06-20T182422.png
security:
- kind: domain-security
  name: Gsk Domain Security
  slug: gsk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gsk Vulnerability Disclosure
  slug: gsk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: gsk
tags:
- Pharmaceuticals
- Biotechnology
- Vaccines
- HIV
- Oncology
- Healthcare
- Clinical Trials
use_cases:
- description: Find and link GSK-sponsored studies into clinical research and evidence-generation platforms via the GSK Study Register and ClinicalTrials.gov.
  name: Clinical Research Data Discovery
- description: Researchers combine GSK trial data accessed through CSDR with external real-world evidence sources for secondary analyses.
  name: Real-World Evidence Studies
- description: Public health agencies and academic groups track Shingrix, Arexvy RSV, and other GSK vaccine outcomes via published trial results.
  name: Vaccine Surveillance
- description: Researchers integrate ViiV Healthcare HIV trial registrations and publications into HIV evidence platforms.
  name: HIV Research
- description: Pharma and CRO biostatistics teams adopt GSK-Biostatistics R packages (tfrmt, gto, slushy) for CDISC-aligned clinical report tables.
  name: Clinical Reporting Automation
- description: Distributors integrate order, shipment, and chargeback flows with GSK's commercial supply chain via X12 EDI.
  name: Pharma Supply Chain Integration
- description: HCPs and medical-information vendors retrieve dosing, contraindication, and interaction information via gskpro.com.
  name: Medical Affairs Engagement
- description: Investors and rating agencies consume GSK's Annual Report, Nature Report, and Modern Slavery Act statement for ESG due diligence.
  name: ESG & Sustainability Reporting
website: https://www.gsk.com
---
