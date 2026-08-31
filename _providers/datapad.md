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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/datapad-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/datapad-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datapad-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://datapad.io/security
- group: company
  title: ''
  type: Website
  url: https://datapad.io
- group: docs
  title: ''
  type: Documentation
  url: https://datapad.io/docs
- group: company
  title: ''
  type: Blog
  url: https://datapad.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://datapad.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.datapad.io
- group: start
  title: ''
  type: Login
  url: https://app.datapad.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://datapad.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datapad.io/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:hello@datapad.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/datapad
- group: auth
  title: ''
  type: Compliance
  url: https://datapad.io/security
- group: design
  title: ''
  type: Conformance
  url: conformance/datapad-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/datapad-llms.txt
created: '2026-07-17'
description: Datapad is an autonomous AI data analyst platform that lets business teams analyze their data by asking questions in natural language. It connects to 50+ data sources — SQL databases, BigQuery, Snowflake, Google Ads, Facebook Ads, Shopify, HubSpot and more — and uses Text2SQL and Python code generation (powered by models such as Claude and ChatGPT) to turn questions into queries, dashboards, and insights, with a Slack bot for conversational analytics. Datapad is a San Francisco company backed by a16z. It is an end-user SaaS product and does not currently publish a public developer REST/GraphQL API, SDKs, or webhook surface; this profile captures its identity, security, and compliance posture.
image: https://datapad.io/images/og-image.png
layout: provider
modified: '2026-07-18'
name: Datapad
nav: Providers
network: true
overview: 'Datapad is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, Artificial Intelligence, Data, and Business Intelligence.


  Datapad''s developer surface includes documentation, engineering blog, pricing, signup flow, support, and 12 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 25.1
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datapad/refs/heads/main/screenshots/datapad-2026-07-25T211346.png
security:
- kind: domain-security
  name: Datapad Domain Security
  slug: datapad-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Datapad Vulnerability Disclosure
  slug: datapad-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Datapad Trust Center
  slug: datapad-trust-center
  summary_line: SOC 2, GDPR
slug: datapad
tags:
- Company
- Analytics
- Artificial Intelligence
- Data
- Business Intelligence
- Natural Language
- Dashboards
- Software-as-a-Service
website: https://datapad.io
---
