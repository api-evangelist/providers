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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 19
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/axsome-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.axsome.com/
- group: company
  title: ''
  type: About
  url: https://www.axsome.com/about/
- group: other
  title: ''
  type: Products
  url: https://www.axsome.com/products/
- group: other
  title: ''
  type: Pipeline
  url: https://www.axsome.com/pipeline/
- group: other
  title: ''
  type: Science
  url: https://www.axsome.com/science/
- group: other
  title: ''
  type: Publications
  url: https://www.axsome.com/publications/
- group: other
  title: ''
  type: MedicalInformation
  url: https://www.axsome.com/medical-information-us/
- group: other
  title: ''
  type: MedicalInformationCanada
  url: https://www.axsome.com/medical-information-canada/
- group: other
  title: ''
  type: ExpandedAccessPolicy
  url: https://www.axsome.com/expanded-access-policy/
- group: company
  title: ''
  type: Careers
  url: https://www.axsome.com/careers/
- group: company
  title: ''
  type: Investors
  url: https://www.axsome.com/investors/
- group: company
  title: ''
  type: NewsRoom
  url: https://www.axsome.com/news-events/
- group: other
  title: ''
  type: RSS
  url: https://www.axsome.com/feed/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.axsome.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.axsome.com/privacy-notice/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.axsome.com/terms-of-use/
- group: auth
  title: ''
  type: StateDisclosures
  url: https://www.axsome.com/state-disclosures/
- group: other
  title: ''
  type: IntellectualProperty
  url: https://www.axsome.com/intellectual-property/
- group: other
  title: ''
  type: ManagementTeam
  url: https://www.axsome.com/management-team/
- group: other
  title: ''
  type: BoardOfDirectors
  url: https://www.axsome.com/board-of-directors/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/axsome-therapeutics
- group: other
  title: ''
  type: StockSymbol
  url: https://www.nasdaq.com/market-activity/stocks/axsm
- group: other
  title: ''
  type: SECFilings
  url: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001579428&type=10-K
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/axsome-therapeutics/refs/heads/main/vocabulary/axsome-therapeutics-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/axsome-therapeutics/refs/heads/main/json-ld/axsome-therapeutics-context.jsonld
- group: other
  title: ''
  type: ProductsList
  url: ''
- group: other
  title: ''
  type: PipelineList
  url: ''
- group: other
  title: ''
  type: ConditionsInFocus
  url: ''
- group: other
  title: ''
  type: Address
  url: ''
created: '2026-05-23'
description: 'Axsome Therapeutics (NASDAQ: AXSM) is a biopharmaceutical company developing and delivering novel therapies for the management of central nervous system (CNS) disorders. Headquartered at One World Trade Center, New York, Axsome markets three FDA-approved products — Auvelity (dextromethorphan-bupropion) for major depressive disorder, Sunosi (solriamfetol) for excessive daytime sleepiness in narcolepsy and obstructive sleep apnea, and Symbravo (meloxicam-rizatriptan) for the acute treatment of migraine — and is advancing a pipeline including AXS-05 for Alzheimer''s disease agitation and smoking cessation, AXS-12 (reboxetine) for narcolepsy, and AXS-14 (esreboxetine) for fibromyalgia. Axsome operates a corporate website and product / HCP microsites but does not expose a public developer API surface; this profile catalogs corporate, product, regulatory, and investor touchpoints rather than programmatic interfaces.'
features:
- description: Exclusive focus on central nervous system disorders spanning psychiatric, neurologic, and sleep-wake conditions.
  name: CNS Therapeutic Focus
- description: Portfolio leverages combinations and single enantiomers acting on NMDA, sigma-1, monoamine reuptake, TAAR1, 5-HT, and GABA targets.
  name: Multi-Mechanistic Small Molecules
- description: Auvelity, Sunosi, and Symbravo are commercially marketed in the United States with sales force and patient support infrastructure.
  name: Commercial Stage with Three Approved Products
- description: Pipeline candidates AXS-05, AXS-12, and AXS-14 address Alzheimer's disease agitation, narcolepsy, fibromyalgia, and smoking cessation.
  name: Active Late-Stage Pipeline
- description: Quarterly earnings, SEC filings (10-K, 10-Q, 8-K), webcasts, presentations, and analyst coverage published on the corporate site and EDGAR.
  name: Investor Disclosure
- description: U.S. and Canada medical-information request channels for healthcare professionals and patients.
  name: Medical Information Services
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/axsome-therapeutics.png
integrations:
- description: Regulatory submissions and approvals for NDA, sNDA, and post-marketing commitments covering Auvelity, Sunosi, Symbravo, and AXS-05.
  name: U.S. Food and Drug Administration (FDA)
- description: Sunosi (solriamfetol) maintains EMA authorization with SmPC and PIL published on the EMA website.
  name: European Medicines Agency (EMA)
- description: Sunosi (solriamfetol) is approved in Canada with English and French product monographs and prescribing information.
  name: Health Canada
- description: Listed on NASDAQ as AXSM; periodic and current reports filed via EDGAR.
  name: NASDAQ / U.S. SEC
- description: U.S. distribution of branded CNS therapies through specialty and retail pharmacy partners.
  name: Specialty Pharmacy Networks
- description: Brand-specific patient support, copay assistance, and access services delivered via HCP and patient microsites.
  name: Patient Support and Copay Programs
jsonld:
- class_count: 26
  name: Axsome Therapeutics Context
  property_count: 14
  slug: axsome-therapeutics-context
layout: provider
modified: '2026-05-23'
name: Axsome Therapeutics
nav: Providers
network: true
overview: 'Axsome Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biopharmaceuticals, Biotechnology, Pharmaceuticals, Healthcare, and Life Sciences.


  The Axsome Therapeutics catalog on APIs.io includes 1 JSON-LD context.'
random_paper: 0
score:
  band: emerging
  composite: 15.7
  delta: -0.5
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 15.2
    contract_quality: 15.5
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 15.2
    operational_transparency: 0.0
  previous_composite: 16.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/axsome-therapeutics/refs/heads/main/screenshots/axsome-therapeutics-2026-06-20T172821.png
security:
- kind: domain-security
  name: Axsome Therapeutics Domain Security
  slug: axsome-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: axsome-therapeutics
tags:
- Biopharmaceuticals
- Biotechnology
- Pharmaceuticals
- Healthcare
- Life Sciences
- Neuroscience
- Central Nervous System
- Depression
- Migraine
- Narcolepsy
- Alzheimers Disease Agitation
- Fibromyalgia
- Smoking Cessation
- Clinical Pipeline
- FDA Approved
use_cases:
- description: HCP microsites for each marketed product provide prescribing information, dosing, safety, and access support.
  name: Healthcare Professional Prescribing
- description: Patient-facing brand sites with medication guides, copay assistance, and condition education.
  name: Patient Access and Adherence
- description: Public disclosures, regulatory filings, and press releases for shareholders, analysts, and financial-data consumers.
  name: Investor Relations
- description: Publications, congress presentations, and medical-affairs touchpoints for the clinical and scientific community.
  name: Scientific Communication
- description: Expanded Access Policy and trial-related communications for investigators and patients seeking access to investigational therapies.
  name: Clinical Trial Engagement
website: https://www.axsome.com/
---
