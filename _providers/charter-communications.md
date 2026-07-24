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
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Charter Communications Agentic Access
  operation_count: 6
  slug: charter-communications-agentic-access
  summary_line: 6 operations · 1 acting
api_count: 4
apis:
- description: Connected device operations
  name: Charter Communications Devices API
  slug: charter-communications-devices-api
- description: Network status operations
  name: Charter Communications Network API
  slug: charter-communications-network-api
- description: Carrier serviceability operations
  name: Charter Communications Serviceability API
  slug: charter-communications-serviceability-api
- description: Service ticket operations
  name: Charter Communications Tickets API
  slug: charter-communications-tickets-api
artifact_total: 15
collections:
- collection_type: open
  name: Charter Communications Bryte IQ API
  slug: open-charter-communications-bryte-iq-api
- collection_type: open
  name: Charter Communications Spectrum Enterprise API
  slug: open-charter-communications-spectrum-enterprise-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/charter-communications-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/charter-communications-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/charter-communications
- group: company
  title: ''
  type: Website
  url: https://corporate.charter.com/
- group: other
  title: ''
  type: ConsumerSite
  url: https://www.spectrum.com/
- group: other
  title: ''
  type: EnterpriseSite
  url: https://enterprise.spectrum.com/
- group: company
  title: ''
  type: Newsroom
  url: https://corporate.charter.com/newsroom
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.charter.com/
- group: company
  title: ''
  type: Careers
  url: https://jobs.spectrum.com/
- group: operate
  title: ''
  type: Support
  url: https://www.spectrum.net/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.spectrum.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.spectrum.com/policies/your-privacy-rights
- group: design
  title: ''
  type: JSONLD
  url: json-ld/charter-communications-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/charter-communications-ticket-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/charter-communications-serviceability-schema.json
created: '2026-03-21'
description: Charter Communications, Inc. is a leading broadband connectivity company and cable operator serving more than 32 million customers in 41 states through its Spectrum brand. Charter offers internet, TV, mobile, and voice services to residential and business customers, and exposes developer APIs through the Spectrum Enterprise portal for service ticketing and carrier serviceability, and through the Bryte IQ Network-as-a-Service platform built on the Linux Foundation CAMARA project.
finops:
- name: Charter Communications Finops
  service_category: Telecommunications / Broadband
  slug: charter-communications-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/charter-communications.png
json_schemas:
- name: Spectrum Enterprise Serviceability
  property_count: 3
  slug: charter-communications-serviceability
- name: Spectrum Enterprise Service Ticket
  property_count: 8
  slug: charter-communications-ticket
jsonld:
- class_count: 0
  name: Charter Communications Context
  property_count: 4
  slug: charter-communications-context
layout: provider
modified: '2026-05-19'
name: Charter Communications
nav: Providers
network: true
overview: 'Charter Communications publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Devices API, Network API, Serviceability API, and 1 more. Tagged areas include Broadband, Cable, CAMARA, Enterprise, and Network as a Service.


  The Charter Communications catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Charter Communications'' developer surface includes support and 14 more developer resources.'
plans:
- name: Charter Communications Plans Pricing
  plan_count: 2
  slug: charter-communications-plans-pricing
press:
- date: '2026-05-25'
  title: SPECTRUM BUSINESS AND RINGCENTRAL EXPAND ...
  url: https://www.prnewswire.com/news-releases/spectrum-business-and-ringcentral-expand-partnership-with-ai-contact-center-and-conversation-intelligence-to-transform-customer-experiences-302711074.html
- date: '2026-05-25'
  title: Charter Announces Strategic Collaboration With AWS
  url: https://corporate.charter.com/newsroom/charter-strategic-collaboration-with-amazon-web-services
- date: '2026-05-25'
  title: Charter Communications Launches Spectrum Voice ID ...
  url: https://corporate.charter.com/newsroom/charter-communications-launches-spectrum-voice-id-accelerates-ai-use-to-enhance-customer-experience
- date: '2026-05-25'
  title: Spectrum Reach Introduces AI Ad Platform with Waymark
  url: https://corporate.charter.com/newsroom/spectrum-reach-introduces-ai-ad-platform-with-waymark
- date: '2026-05-25'
  title: 'AI Inside: Artificial Intelligence for Network and Customer ...'
  url: https://techexpo.scte.org/session/ai-inside-artificial-intelligence-for-network-and-customer-experience-innovation/
random_paper: 8
rate_limits:
- limit_count: 2
  name: Charter Communications Rate Limits
  slug: charter-communications-rate-limits
rules:
- name: Charter Communications API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: charter-communications-jsonschema-spectral-rules
score:
  band: thin
  composite: 42.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 54.9
    developer_ergonomics: 4.3
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 21.1
  previous_composite: 42.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/charter-communications/refs/heads/main/screenshots/charter-communications-2026-06-20T174233.png
security:
- kind: domain-security
  name: Charter Communications Domain Security
  slug: charter-communications-domain-security
  summary_line: TLSv1.3 · DMARC
slug: charter-communications
tags:
- Broadband
- Cable
- CAMARA
- Enterprise
- Network as a Service
- NaaS
- Spectrum
- Telecommunications
- Ticketing
- Fortune 500
website: https://corporate.charter.com/
---
