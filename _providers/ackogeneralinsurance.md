---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-09-06'
api_count: 1
apis:
- baseURL: https://www.acko.com
  baseurl_source: declared
  description: Embedded-insurance partnership API for issuing, endorsing, retrieving and claiming against ACKO policies. Covers credit life and loan-shield, trip, gig-workforce, group health, house, fire, cyber prot
  name: ACKO for Enterprise Partnership API
  slug: acko-for-enterprise-partnership-api
artifact_total: 6
asyncapis:
- description: ''
  name: Ackogeneralinsurance Webhooks
  slug: ackogeneralinsurance-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.acko.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.acko.com/gi/enterprise/
- group: docs
  title: ''
  type: Documentation
  url: https://www.acko.com/enterprise/documentation/enterprise.html
- group: docs
  title: ''
  type: APIReference
  url: https://www.acko.com/enterprise/documentation/enterprise.html
- group: operate
  title: ''
  type: Support
  url: https://www.acko.com/contact-us/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.acko.com/gi/customer-service/
- group: company
  title: ''
  type: Blog
  url: https://www.acko.com/articles/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.acko.com/gi/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acko.com/gi/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.acko.com/gi/public-disclosure/
- group: auth
  title: ''
  type: Authentication
  url: authentication/ackogeneralinsurance-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ackogeneralinsurance-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/ackogeneralinsurance-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ackogeneralinsurance-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ackogeneralinsurance-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ackogeneralinsurance-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ackogeneralinsurance-lifecycle.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ackogeneralinsurance-enterprise-overlay.yaml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ackogeneralinsurance-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ackogeneralinsurance-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/ackogeneralinsurance-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ackogeneralinsurance-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ackogeneralinsurance-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ackogeneralinsurance-domain-security.yml
created: '2026-09-06'
description: ACKO General Insurance Limited is an India-based digital-first general insurer (IRDAI registration number 157, CIN U66000KA2016PLC138288) selling car, bike, health, travel, home and device cover direct to consumers, and embedding insurance into partner platforms through ACKO for Business. Its enterprise partnership API stack issues, endorses, retrieves and files claims against policies for credit and loan protection, gig-workforce cover, group health, trip, home, fire, cyber protection and electronic-device products. The partnership surface is published as a public OpenAPI 3.0.1 contract of 30 operations across issuance, proposal, endorsement, policy retrieval and claims, authenticated with OAuth 2.0 client-credential tokens issued from a Keycloak partnership realm.
image: https://acko-cms.ackoassets.com/logo_flat_darktext_lightbg_horizontal_notagline_c93af46624.png
layout: provider
modified: '2026-09-06'
name: ACKO General Insurance
nav: Providers
network: true
overview: 'ACKO General Insurance publishes 1 API on the [APIs.io](https://apis.io/) network: ACKO for Enterprise Partnership API. Tagged areas include Insurance, Insurtech, Embedded Insurance, Health Insurance, and Travel Insurance.


  The ACKO General Insurance catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ACKO General Insurance''s developer surface includes documentation, API reference, support, engineering blog, authentication, and 20 more developer resources.'
plans:
- name: Ackogeneralinsurance Plans Pricing
  plan_count: 0
  slug: ackogeneralinsurance-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Ackogeneralinsurance Rate Limits
  slug: ackogeneralinsurance-rate-limits
score:
  band: developing
  composite: 41.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 4.5
    contract_quality: 56.4
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.19.0
  scored_at: '2026-09-06'
security:
- kind: authentication
  name: Ackogeneralinsurance Authentication
  slug: ackogeneralinsurance-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Ackogeneralinsurance Domain Security
  slug: ackogeneralinsurance-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: ackogeneralinsurance
tags:
- Insurance
- Insurtech
- Embedded Insurance
- Health Insurance
- Travel Insurance
- Claims
- Policy Administration
- Financial Services
- India
- Enterprise
website: https://www.acko.com/
---
