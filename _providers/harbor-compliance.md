---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Harbor Compliance Agentic Access
  operation_count: 18
  slug: harbor-compliance-agentic-access
  summary_line: 18 operations · 5 acting
api_count: 1
apis:
- description: Annual reports, compliance filings, and deadline tracking.
  name: Harbor Compliance Compliance Filings API
  slug: harbor-compliance-compliance-filings-api
- description: Business entity management including corporations, LLCs, and other legal entities.
  name: Harbor Compliance Entities API
  slug: harbor-compliance-entities-api
- description: State and jurisdiction information for compliance requirements.
  name: Harbor Compliance Jurisdictions API
  slug: harbor-compliance-jurisdictions-api
- description: Business license applications, renewals, and status tracking across jurisdictions.
  name: Harbor Compliance Licenses API
  slug: harbor-compliance-licenses-api
- description: Compliance service orders and fulfillment tracking.
  name: Harbor Compliance Orders API
  slug: harbor-compliance-orders-api
- description: Registered agent appointment and management for business entities.
  name: Harbor Compliance Registered Agents API
  slug: harbor-compliance-registered-agents-api
artifact_total: 29
collections:
- collection_type: postman
  name: Harbor Compliance Compliance Filings API
  slug: postman-harbor-compliance-compliance-filings-api
- collection_type: postman
  name: Harbor Compliance Compliance Filings Entities API
  slug: postman-harbor-compliance-entities-api
- collection_type: postman
  name: Harbor Compliance Compliance Filings Jurisdictions API
  slug: postman-harbor-compliance-jurisdictions-api
- collection_type: postman
  name: Harbor Compliance Compliance Filings Licenses API
  slug: postman-harbor-compliance-licenses-api
- collection_type: postman
  name: Harbor Compliance Compliance Filings Orders API
  slug: postman-harbor-compliance-orders-api
- collection_type: postman
  name: Harbor Compliance Compliance Filings Registered Agents API
  slug: postman-harbor-compliance-registered-agents-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Harbor Compliance Compliance Filings API
  slug: open-harbor-compliance-compliance-filings-api
- collection_type: open
  name: Harbor Compliance Compliance Filings Entities API
  slug: open-harbor-compliance-entities-api
- collection_type: open
  name: Harbor Compliance Compliance Filings Jurisdictions API
  slug: open-harbor-compliance-jurisdictions-api
- collection_type: open
  name: Harbor Compliance Compliance Filings Licenses API
  slug: open-harbor-compliance-licenses-api
- collection_type: open
  name: Harbor Compliance Compliance Filings Orders API
  slug: open-harbor-compliance-orders-api
- collection_type: open
  name: Harbor Compliance Compliance Filings Registered Agents API
  slug: open-harbor-compliance-registered-agents-api
- collection_type: open
  name: Harbor Compliance API
  slug: open-harbor-compliance
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/harbor-compliance/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/harbor-compliance-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/harbor-compliance-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/harbor-compliance-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/harbor-compliance
- group: start
  title: ''
  type: Portal
  url: https://developers.harborcompliance.com/
- group: company
  title: ''
  type: Website
  url: https://www.harborcompliance.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.harborcompliance.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.harborcompliance.com/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.harborcompliance.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.harborcompliance.com/contact
- group: start
  title: ''
  type: Login
  url: https://www.harborcompliance.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.harborcompliance.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.harborcompliance.com/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.harborcompliance.com/security
- group: design
  title: ''
  type: JSONLD
  url: json-ld/harbor-compliance-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/harbor-compliance-entity-schema.json
created: '2025-02-17'
description: Harbor Compliance is a compliance management platform that helps businesses streamline compliance workflows, save staff hours, and enhance client relationships. The platform provides tools for managing business licensing, registered agent services, and compliance tracking.
finops:
- name: Harbor Compliance Finops
  service_category: API
  slug: harbor-compliance-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/harbor-compliance.png
json_schemas:
- name: Harbor Compliance Business Entity
  property_count: 12
  slug: harbor-compliance-entity
jsonld:
- class_count: 0
  name: Harbor Compliance Context
  property_count: 5
  slug: harbor-compliance-context
layout: provider
modified: '2026-05-19'
name: Harbor Compliance
nav: Providers
network: true
overview: 'Harbor Compliance publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Compliance Filings API, Entities API, Jurisdictions API, and 3 more. Tagged areas include Business Licensing, Compliance, Legal, and Regulatory.


  The Harbor Compliance catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Harbor Compliance''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, support, and 11 more developer resources.'
plans:
- name: Harbor Compliance Plans Pricing
  plan_count: 3
  slug: harbor-compliance-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Harbor Compliance Rate Limits
  slug: harbor-compliance-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Harbor Compliance API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: harbor-compliance-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.6
  coverage:
    artifact_dirs: 14
    catalog_gap: 64.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 9.8
    contract_quality: 65.6
    developer_ergonomics: 54.8
    discoverability: 50.0
    governance: 9.8
    operational_transparency: 18.4
  previous_composite: 44.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/harbor-compliance/refs/heads/main/screenshots/harbor-compliance-2026-06-20T182514.png
security:
- kind: authentication
  name: Harbor Compliance Authentication
  slug: harbor-compliance-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Harbor Compliance Domain Security
  slug: harbor-compliance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: harbor-compliance
tags:
- Business Licensing
- Compliance
- Legal
- Regulatory
website: https://www.harborcompliance.com/
---
