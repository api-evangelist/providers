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
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Amgen discovers, develops, manufactures, and delivers innovative biologic medicines for patients with serious illnesses. The company does not currently publish a public developer API.
  name: Amgen Website
  slug: website
artifact_total: 19
common:
- group: build
  title: ''
  type: Packages
  url: packages/amgen-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amgen-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amgen-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Amgen
- group: company
  title: ''
  type: Website
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
  url: https://www.amgen.com/contact-us
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
coverage:
  checked: '2026-09-02'
  detail: 'Amgen manufactures biologic medicines, not software: its full 2,773-URL corporate sitemap contains no developer, API or documentation section, /developers and /openapi.json both 404, the whole /.well-known/ directory is 403 at the edge, and api.amgen.com resolves only to a shared Salesforce Commerce Cloud host serving an unrelated tenant.'
  evidence:
  - status: 200
    url: https://www.amgen.com/sitemap.xml
  - status: 404
    url: https://www.amgen.com/developers
  - status: 404
    url: https://www.amgen.com/openapi.json
  - status: 403
    url: https://www.amgen.com/.well-known/api-catalog
  - status: 403
    url: https://www.amgen.com/graphql
  reason: not-a-software-company
  state: none
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
modified: '2026-09-02'
name: Amgen
nav: Providers
network: true
overview: 'Amgen publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Biopharmaceutical, Oncology, inflammation, and Cardiovascular.


  Amgen''s developer surface includes engineering blog, support, YouTube channel, and 9 more developer resources.'
plans:
- name: Amgen Plans Pricing
  plan_count: 0
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
random_paper: 16
rate_limits:
- limit_count: 0
  name: Amgen Rate Limits
  slug: amgen-rate-limits
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 13.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- inflammation
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
