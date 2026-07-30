---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: At Bay Agentic Access
  operation_count: 12
  slug: at-bay-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 5
apis:
- description: Upload submission documents and download generated policy documents.
  name: At-Bay Documents API
  slug: at-bay-documents-api
- description: API health check.
  name: At-Bay Health API
  slug: at-bay-health-api
- description: Manage bound policies including renewal behavior.
  name: At-Bay Policies API
  slug: at-bay-policies-api
- description: Create, poll, and bind insurance quotes.
  name: At-Bay Quotes API
  slug: at-bay-quotes-api
- description: Register webhook endpoints for asynchronous status callbacks.
  name: At-Bay Webhooks API
  slug: at-bay-webhooks-api
artifact_total: 21
collections:
- collection_type: open
  name: At-Bay Partner API
  slug: open-at-bay-partner-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/at-bay-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/at-bay-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/at-bay-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.at-bay.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.at-bay.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.at-bay.com/docs/getting-started
- group: docs
  title: ''
  type: Reference
  url: https://developers.at-bay.com/reference
- group: agent
  title: ''
  type: LLMs
  url: https://developers.at-bay.com/llms.txt
- group: company
  title: ''
  type: Partnerships
  url: https://www.at-bay.com/about/partnerships/
- group: other
  title: ''
  type: Brokers
  url: https://www.at-bay.com/brokers/
- group: other
  title: ''
  type: BrokerPlatform
  url: https://www.at-bay.com/brokers/platform/
- group: other
  title: ''
  type: Insurance
  url: https://www.at-bay.com/insurance/
- group: other
  title: ''
  type: CyberInsurance
  url: https://www.at-bay.com/insurance/cyber/
- group: other
  title: ''
  type: TechEO
  url: https://www.at-bay.com/insurance/tech-eo/
- group: other
  title: ''
  type: MPL
  url: https://www.at-bay.com/insurance/mpl/
- group: other
  title: ''
  type: Stance
  url: https://www.at-bay.com/stance/
- group: other
  title: ''
  type: MDR
  url: https://www.at-bay.com/stance/mdr/
- group: operate
  title: ''
  type: IncidentResponse
  url: https://www.at-bay.com/stance/incident-response/
- group: company
  title: ''
  type: Newsroom
  url: https://www.at-bay.com/news/
- group: company
  title: ''
  type: About
  url: https://www.at-bay.com/about/
- group: company
  title: ''
  type: Careers
  url: https://www.at-bay.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.at-bay.com/contact/
- group: start
  title: ''
  type: Login
  url: https://platform.at-bay.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/at-bay
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/at-bay-insurance
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/AtBayInsurance
- group: commercial
  title: ''
  type: Plans
  url: plans/at-bay-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/at-bay-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/at-bay-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/at-bay-vocabulary.yml
created: '2026-05-25'
description: At-Bay is an InsurSec company that combines cyber insurance with proactive security monitoring for businesses. Headquartered in New York with offices in San Francisco and Tel Aviv, At-Bay underwrites Surplus Cyber, Surplus Tech E&O, and Surplus Miscellaneous Professional Liability (MPL) coverage and bundles them with the At-Bay Stance security platform (advisory, fraud defense, incident response) and 24/7 Managed Detection and Response (MDR) across endpoint, email (MXDR), and multi-vector surfaces. At-Bay distributes through a network of independent brokers and partners and exposes a production-grade REST Partner API (v2) that lets brokerage platforms, digital distributors, and agency management systems quote, customize, bind, renew, retrieve documents, and receive webhook callbacks for the full policy lifecycle. Demo environment at api-demo.at-bay.com lets partners integrate without going through Broker of Record clearance.
examples:
- key_count: 2
  name: At Bay Create Quote Example
  slug: at-bay-create-quote-example
- key_count: 2
  name: At Bay Get Quote Example
  slug: at-bay-get-quote-example
- key_count: 2
  name: At Bay Register Webhook Example
  slug: at-bay-register-webhook-example
finops:
- name: At Bay Finops
  service_category: ''
  slug: at-bay-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/at-bay.png
json_schemas:
- name: At-Bay Policy
  property_count: 13
  slug: at-bay-policy
- name: At-Bay Quote
  property_count: 10
  slug: at-bay-quote
json_structures:
- name: At Bay Quote Structure
  property_count: 0
  slug: at-bay-quote-structure
jsonld:
- class_count: 31
  name: At Bay Context
  property_count: 0
  slug: at-bay-context
layout: provider
modified: '2026-05-25'
name: At-Bay
nav: Providers
network: true
overview: 'At-Bay publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Documents API, Health API, Policies API, and 2 more. Tagged areas include Insurance, Cyber Insurance, InsurSec, Insurtech, and Tech E&O.


  The At-Bay catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  At-Bay''s developer surface includes authentication, documentation, GitHub presence, and 27 more developer resources.'
plans:
- name: At Bay Plans Pricing
  plan_count: 4
  slug: at-bay-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: At Bay Rate Limits
  slug: at-bay-rate-limits
rules:
- name: At-Bay API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: at-bay-jsonschema-spectral-rules
- name: At-Bay API Rules
  rule_count: 5
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 2
  slug: at-bay-rules
score:
  band: developing
  composite: 48.2
  delta: -5.6
  facets:
    commercial_clarity: 52.6
    contract_quality: 73.4
    developer_ergonomics: 34.8
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 53.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 25.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/at-bay/refs/heads/main/screenshots/at-bay-2026-06-20T172516.png
security:
- kind: authentication
  name: At Bay Authentication
  slug: at-bay-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: At Bay Domain Security
  slug: at-bay-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: at-bay
tags:
- Insurance
- Cyber Insurance
- InsurSec
- Insurtech
- Tech E&O
- Professional Liability
- MPL
- Managed Detection And Response
- MDR
- Security Monitoring
- Email Security
- Endpoint Security
- Incident Response
- Brokers
- Quoting
- Binding
- Policy Lifecycle
- Webhooks
website: https://www.at-bay.com
---
