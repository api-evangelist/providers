---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: 'Rite Aid supports Electronic Data Interchange (EDI) for vendor integration using ANSI/ASC X12 standards (versions 4010 and 5010). Supported transactions include purchase orders (850), invoices (810), '
  name: Rite Aid EDI Integration
  slug: edi-integration
- description: Rite Aid's digital health platform includes an AI health assistant for informational health queries, pharmacy services with prescription transfer and records management, vaccination record access, and
  name: Rite Aid Digital Health Services
  slug: digital-health
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rite-aid-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Rite-Aid
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/riteaid
- group: company
  title: ''
  type: Website
  url: https://www.rite-aid.com
- group: start
  title: ''
  type: EDIPortal
  url: https://raportal.riteaid.com/
- group: other
  title: ''
  type: EDIServices
  url: https://www.riteaidediservices.com/
- group: other
  title: ''
  type: MobileApp
  url: https://riteaid.com/app
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.riteaid.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.riteaid.com/terms-of-use
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/rite-aid/refs/heads/main/json-schema/rite-aid-edi-transaction-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/rite-aid/refs/heads/main/json-ld/rite-aid-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/rite-aid/refs/heads/main/vocabulary/rite-aid-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://rite-aid.com/llms.txt
created: '2026-03-24'
description: Rite Aid is one of the nation's leading drugstore chains, providing prescription drugs, health and beauty aids, and convenience items. Rite Aid supports vendor integrations through EDI (Electronic Data Interchange) and B2B services, and offers digital health tools including an AI health assistant, pharmacy services, vaccination record management, and preventive health screening programs.
finops:
- name: Rite Aid Finops
  service_category: Retail / Pharmacy
  slug: rite-aid-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rite-aid.png
json_schemas:
- name: Rite Aid EDI Transaction
  property_count: 9
  slug: rite-aid-edi-transaction
json_structures:
- name: Rite Aid Edi Transaction Structure
  property_count: 0
  slug: rite-aid-edi-transaction-structure
jsonld:
- class_count: 34
  name: Rite Aid Context
  property_count: 0
  slug: rite-aid-context
layout: provider
modified: '2026-05-02'
name: Rite Aid
nav: Providers
network: true
overview: 'Rite Aid publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include EDI, Fortune 500, Health, Pharmacy, and Prescriptions.


  The Rite Aid catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Rite Aid Plans Pricing
  plan_count: 1
  slug: rite-aid-plans-pricing
press:
- date: '2026-05-25'
  title: Leveraging Artificial Intelligence to Transform US Retail ...
  url: https://gprjournals.org/journals/index.php/ajt/article/view/456
- date: '2026-05-25'
  title: Rite Aid to face five-year facial recognition technology ban
  url: https://www.youtube.com/watch?v=k4hkQrkVMZQ
- date: '2026-05-25'
  title: The FTC's Case Against Rite Aid's Deployment of AI-Based ...
  url: https://www.arnoldporter.com/en/perspectives/advisories/2024/01/ftc-case-against-rite-aid-deployment-of-ai-based-technology
- date: '2026-05-25'
  title: Rite Aid and Google Cloud Partner to Modernize Pharmacy ...
  url: https://www.prnewswire.com/news-releases/rite-aid-and-google-cloud-partner-to-modernize-pharmacy-operations-and-enhance-the-online-customer-experience-301645616.html
- date: '2026-05-25'
  title: Rite Aid Banned from Using AI Facial Recognition After ...
  url: https://www.ftc.gov/news-events/news/press-releases/2023/12/rite-aid-banned-using-ai-facial-recognition-after-ftc-says-retailer-deployed-technology-without
random_paper: 6
rate_limits:
- limit_count: 1
  name: Rite Aid Rate Limits
  slug: rite-aid-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Rite Aid API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rite-aid-jsonschema-spectral-rules
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 14
    catalog_gap: 59.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 25.0
    contract_quality: 10.7
    developer_ergonomics: 14.3
    discoverability: 66.7
    governance: 25.0
    operational_transparency: 7.9
  previous_composite: 18.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rite-aid/refs/heads/main/screenshots/rite-aid-2026-06-20T193130.png
security:
- kind: domain-security
  name: Rite Aid Domain Security
  slug: rite-aid-domain-security
  summary_line: TLSv1.3 · HSTS
slug: rite-aid
tags:
- EDI
- Fortune 500
- Health
- Pharmacy
- Prescriptions
- Retail
website: https://www.rite-aid.com
---
