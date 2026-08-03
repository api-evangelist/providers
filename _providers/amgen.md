---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: Amgen discovers, develops, manufactures, and delivers innovative biologic medicines for patients with serious illnesses. The company does not currently publish a public developer API.
  name: Amgen Website
  slug: website
artifact_total: 19
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amgen-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Amgen
- group: start
  title: ''
  type: Portal
  url: https://www.amgen.com
- group: company
  title: ''
  type: Blog
  url: https://www.amgen.com/stories
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amgen.com/privacy-statement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amgen.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.amgen.com/contact-amgen
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/amgen
- group: other
  title: ''
  type: X
  url: https://twitter.com/AmgenNews
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/amgen
created: '2024-01-01'
description: Amgen is committed to unlocking the potential of biology for patients suffering from serious illnesses by discovering, developing, manufacturing and delivering innovative human therapeutics. As a pioneer in biotechnology since 1980, Amgen uses living cells to make biologic medicines addressing cardiovascular metabolic conditions, oncology, inflammation, rare diseases, and bone health, operating in approximately 100 countries worldwide.
features:
- description: Pioneering use of living cells and human genetic data combined with AI and generative biology to discover novel biologic medicines.
  name: Biologic Drug Discovery
- description: Cancer medicines targeting solid tumors and hematologic malignancies including innovative BiTE and antibody therapies.
  name: Oncology Therapeutics
- description: Medicines addressing heart disease, high cholesterol (Lp(a)), obesity, and obesity-related metabolic conditions.
  name: Cardiovascular and Metabolic Medicines
- description: Treatments for inflammatory conditions including chronic rhinosinusitis with nasal polyps, asthma, and other immune-mediated diseases.
  name: Inflammation Therapeutics
- description: Therapies for rare conditions including IgG4-related disease (IgG4-RD), generalized myasthenia gravis, and other orphan indications.
  name: Rare Disease Medicines
- description: Medicines for osteoporosis, bone metastases, and other bone health conditions including PROLIA and XGEVA.
  name: Bone Health Products
- description: High-quality biosimilar medicines providing more affordable alternatives to reference biologic therapies across multiple therapeutic areas.
  name: Biosimilars
- description: Application of artificial intelligence, generative biology, and advanced data science to accelerate drug discovery and clinical trial optimization.
  name: AI-Driven Drug Development
finops:
- name: Amgen Finops
  service_category: Biopharmaceutical
  slug: amgen-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amgen.png
layout: provider
modified: '2026-04-19'
name: Amgen
nav: Providers
network: true
overview: 'Amgen publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Biopharmaceutical, Oncology, Inflammation, and Cardiovascular.


  Amgen''s developer surface includes developer portal, engineering blog, support, YouTube channel, and 6 more developer resources.'
plans:
- name: Amgen Plans Pricing
  plan_count: 1
  slug: amgen-plans-pricing
press:
- date: '2026-05-25'
  title: Artificial Intelligence Vision
  url: https://www.amgen.com/about/how-we-operate/policies-practices-and-disclosures/artificial-intelligence-vision
- date: '2026-05-25'
  title: AI in Research & Development | Amgen
  url: https://www.amgen.com/science/research-and-development-strategy/ai-in-research-and-development
- date: '2026-05-25'
  title: 'Enhanced Patient-Centricity: How the Biopharmaceutical ...'
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9602573/
- date: '2026-05-25'
  title: AMGEN ANNOUNCES RETIREMENT OF DAVID M. ...
  url: https://www.prnewswire.com/news-releases/amgen-announces-retirement-of-david-m-reese-executive-vice-president-and-chief-technology-officer-302750791.html
- date: '2026-05-25'
  title: 'On the Global Stage: Amgen''s Top Voices Drive ...'
  url: https://www.amgen.com/stories/2025/05/on-the-global-stage-amgens-top-voices-drive-conversations-on-ai-and-innovation
random_paper: 45
rate_limits:
- limit_count: 1
  name: Amgen Rate Limits
  slug: amgen-rate-limits
score:
  band: emerging
  composite: 22.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 22.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amgen/refs/heads/main/screenshots/amgen-2026-06-20T171930.png
security:
- kind: domain-security
  name: Amgen Domain Security
  slug: amgen-domain-security
  summary_line: TLSv1.3 · DMARC
slug: amgen
tags:
- Biotechnology
- Biopharmaceutical
- Oncology
- Inflammation
- Cardiovascular
- Rare Disease
- Biosimilars
- Life Sciences
- Fortune 500
use_cases:
- description: Providing oncology medicines for patients with solid tumors and blood cancers through innovative biologic and targeted therapies.
  name: Cancer Treatment
- description: Reducing cardiovascular risk with medicines targeting LDL cholesterol, Lp(a), and other cardiovascular risk factors.
  name: Heart Disease Prevention
- description: Managing chronic inflammatory conditions with targeted biologic therapies for patients with severe unmet medical needs.
  name: Inflammatory Disease Management
- description: Delivering life-changing therapies to patients with rare and ultra-rare diseases where few or no other treatments exist.
  name: Rare Disease Treatment
- description: Improving patient access to biologic therapies through high-quality, lower-cost biosimilar medicines.
  name: Biosimilar Access
- description: Addressing obesity and obesity-related conditions with novel medicines targeting metabolic pathways.
  name: Weight Management
website: https://www.amgen.com
---
