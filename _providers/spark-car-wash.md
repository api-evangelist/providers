---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spark-car-wash-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sparkcarwash.com/
- group: company
  title: ''
  type: Blog
  url: https://sparkcarwash.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://sparkcarwash.com/contact-us/
- group: operate
  title: ''
  type: FAQ
  url: https://sparkcarwash.com/faq-old2/
- group: start
  title: ''
  type: SignUp
  url: https://sparkcw.patheon.app/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sparkcarwash.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sparkcarwash.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spark-car-wash
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spark-car-wash-llms.txt
coverage:
  checked: '2026-08-28'
  detail: Spark Car Wash operates physical express-tunnel car wash sites in NJ/PA/NY and sells unlimited-wash memberships through a third-party portal at sparkcw.patheon.app; its own WordPress site 404s on every OpenAPI, GraphQL, llms.txt and /.well-known/ path, so there is no developer program or contract to profile.
  evidence:
  - status: 404
    url: https://sparkcarwash.com/openapi.json
  - status: 404
    url: https://sparkcarwash.com/graphql
  - status: 404
    url: https://sparkcarwash.com/.well-known/agent-card.json
  - status: 404
    url: https://sparkcarwash.com/llms.txt
  - status: 404
    url: https://sparkcarwash.com/.well-known/security.txt
  reason: not-a-software-company
  state: none
created: '2026-08-28'
description: 'Spark Car Wash is an express-tunnel car wash operator running a network of high-throughput drive-thru locations across New Jersey, Pennsylvania and New York. The company pairs a conveyorized tunnel — neoglide washers, custom non-acidic cleaning formulas, high-intensity dryers, and a closed-loop water reclamation and filtration system — with self-service "Spark Park" terminals offering multi-nozzle vacuums, anti-scratch towels and automated mat cleaners. Revenue is driven by unlimited-wash memberships sold in Standard, Select and Signature tiers, with additional-vehicle discounts, alongside single-wash purchases. Membership signup and account management run on a third-party hosted portal rather than a Spark-operated application. Spark Car Wash is a physical services operator: it publishes no developer program, no public API, no SDKs and no machine-readable contract of any kind.'
image: https://sparkcarwash.com/wp-content/uploads/2023/11/SPARK-Footer-Logo.png
layout: provider
modified: '2026-08-28'
name: Spark Car Wash
nav: Providers
network: true
overview: 'Spark Car Wash is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Car Wash, Automotive Services, Consumer Services, and Retail.


  Spark Car Wash''s developer surface includes engineering blog, support, FAQ, signup flow, and 6 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spark-car-wash/refs/heads/main/screenshots/spark-car-wash-2026-09-02T160332.png
security:
- kind: domain-security
  name: Spark Car Wash Domain Security
  slug: spark-car-wash-domain-security
  summary_line: TLSv1.3 · DMARC
slug: spark-car-wash
tags:
- Company
- Car Wash
- Automotive Services
- Consumer Services
- Retail
- Subscription
- Memberships
- New Jersey
- United States
website: https://sparkcarwash.com/
---
