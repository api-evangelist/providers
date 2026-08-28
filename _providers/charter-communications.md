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
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-08-26'
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
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Charter Communications Bryte IQ API
  slug: open-charter-communications-bryte-iq-api
- collection_type: open
  name: Charter Communications Bryte IQ Devices API
  slug: open-charter-communications-devices-api
- collection_type: open
  name: Charter Communications Bryte IQ Devices Network API
  slug: open-charter-communications-network-api
- collection_type: open
  name: Charter Communications Bryte IQ Devices Serviceability API
  slug: open-charter-communications-serviceability-api
- collection_type: open
  name: Charter Communications Spectrum Enterprise API
  slug: open-charter-communications-spectrum-enterprise-api
- collection_type: open
  name: Charter Communications Bryte IQ Devices Tickets API
  slug: open-charter-communications-tickets-api
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
random_paper: 14
rate_limits:
- limit_count: 2
  name: Charter Communications Rate Limits
  slug: charter-communications-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Charter Communications API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: charter-communications-jsonschema-spectral-rules
score:
  band: emerging
  composite: 26.1
  delta: 0.1
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 9.8
    contract_quality: 49.7
    developer_ergonomics: 4.8
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 5.3
  previous_composite: 26.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 20.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
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
