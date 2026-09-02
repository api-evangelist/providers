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
  band: agent-aware
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 16
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/abbvie-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://cvd.abbvie.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/abbvie-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/abbvie-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/abbvie-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abbvie-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AbbVie
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/abbvie
- group: company
  title: ''
  type: Website
  url: https://www.abbvie.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.abbvie.com/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.abbvie.com/terms-of-use.html
- group: company
  title: ''
  type: Blog
  url: https://news.abbvie.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.abbvie.com/contact-us.html
coverage:
  checked: '2026-08-29'
  detail: 'AbbVie runs a live Apigee Edge gateway at api.abbvie.com that answers every path with "Unable to identify proxy for host: secure" — real API infrastructure with no public proxy, no developer portal, no reference, and a verified GitHub organization carrying zero public repositories.'
  evidence:
  - status: 404
    url: https://api.abbvie.com/openapi.json
  - status: 200
    url: https://api.github.com/orgs/AbbVie
  - status: 200
    url: https://www.abbvieclinicaltrials.com/.well-known/api-catalog
  - status: 403
    url: https://www.abbvie.com/
  reason: no-developer-program
  state: none
created: '2024-01-15'
description: AbbVie is a research-based biopharmaceutical company that discovers, develops, manufactures, and markets advanced therapies in immunology, oncology, neuroscience, and other specialty areas. AbbVie's portfolio includes treatments for autoimmune diseases, various cancers, neurological disorders, and aesthetics through the Allergan Aesthetics portfolio.
features:
- description: Treatments for rheumatoid arthritis, psoriasis, IBD, and other immune-mediated diseases including Humira and Skyrizi
  name: Immunology Portfolio
- description: Hematologic malignancy treatments and solid tumor therapies including Imbruvica and Venclexta
  name: Oncology Pipeline
- description: Treatments for Parkinson's disease, migraine, and psychiatric conditions
  name: Neuroscience Therapeutics
- description: Medical aesthetics products through the Allergan Aesthetics portfolio
  name: Aesthetics Division
- description: Research-based drug discovery leveraging genomics, proteomics, and AI/ML approaches
  name: Drug Discovery Research
image: /assets/icons/abbvie.png
integrations:
- description: Integration with EHR systems for clinical data exchange and prescribing information
  name: Electronic Health Records
- description: Integration with CTMS platforms for clinical trial data collection and management
  name: Clinical Trial Management
- description: Integration with pharmacy and insurance systems for patient access programs
  name: Patient Assistance Programs
layout: provider
modified: '2026-08-29'
name: AbbVie
nav: Providers
network: true
overview: 'AbbVie is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Pharmaceuticals, biopharmaceuticals, Healthcare, Life Sciences, and Drug Discovery.


  AbbVie''s developer surface includes engineering blog and 12 more developer resources.'
plans:
- name: Abbvie Plans Pricing
  plan_count: 0
  slug: abbvie-plans-pricing
press:
- date: '2026-05-25'
  title: Areas of Innovation
  url: https://www.abbvie.com/science/areas-of-innovation.html
- date: '2026-05-25'
  title: Three ways AI is changing drug discovery at AbbVie
  url: https://www.abbvie.com/who-we-are/our-stories/three-ways-ai-is-changing-drug-discovery-at-abbvie.html
- date: '2026-05-25'
  title: AI & Data Convergence
  url: https://www.abbvie.com/science/areas-of-innovation/ai-and-data-convergence.html
- date: '2026-05-25'
  title: AbbVie and BigHat Biosciences Announce Research ...
  url: https://www.prnewswire.com/news-releases/abbvie-and-bighat-biosciences-announce-research-collaboration-to-leverage-artificial-intelligence-and-machine-learning-to-discover-next-generation-therapeutic-antibodies-302006127.html
- date: '2026-05-25'
  title: Artificial Intelligence at AbbVie - Two Use Cases
  url: https://emerj.com/artificial-intelligence-at-abbvie-two-use-cases/
random_paper: 8
rate_limits:
- limit_count: 0
  name: Abbvie Rate Limits
  slug: abbvie-rate-limits
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 10
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/abbvie/refs/heads/main/screenshots/abbvie-2026-06-20T163132.png
security:
- kind: domain-security
  name: Abbvie Domain Security
  slug: abbvie-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Abbvie Vulnerability Disclosure
  slug: abbvie-vulnerability-disclosure
  summary_line: Hackerone
slug: abbvie
tags:
- Pharmaceuticals
- biopharmaceuticals
- Healthcare
- Life Sciences
- Drug Discovery
- Fortune 500
use_cases:
- description: Access clinical trial results and outcomes data for research and regulatory submissions
  name: Clinical Trial Data
- description: Connect patient access programs and medication assistance with healthcare systems
  name: Patient Support Programs
- description: Provide healthcare professionals with product information and medical affairs resources
  name: Healthcare Provider Portals
- description: Collect and analyze real-world patient data for post-market surveillance
  name: Real World Evidence
website: https://www.abbvie.com/
---
