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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Qualtrics Agentic Access
  operation_count: 22
  slug: qualtrics-agentic-access
  summary_line: 22 operations · 10 acting
api_count: 3
apis:
- description: The automations API from Qualtrics — 1 operation(s) for automations.
  name: Qualtrics automations API
  slug: qualtrics-automations-api
- description: The Directories API from Qualtrics — 1 operation(s) for directories.
  name: Qualtrics Directories API
  slug: qualtrics-directories-api
- description: The Distributions API from Qualtrics — 2 operation(s) for distributions.
  name: Qualtrics Distributions API
  slug: qualtrics-distributions-api
- description: The Eventsubscriptions API from Qualtrics — 3 operation(s) for eventsubscriptions.
  name: Qualtrics Eventsubscriptions API
  slug: qualtrics-eventsubscriptions-api
- description: The file API from Qualtrics — 3 operation(s) for file.
  name: Qualtrics file API
  slug: qualtrics-file-api
- description: The files API from Qualtrics — 1 operation(s) for files.
  name: Qualtrics files API
  slug: qualtrics-files-api
- description: The Survey Definitions API from Qualtrics — 2 operation(s) for survey definitions.
  name: Qualtrics Survey Definitions API
  slug: qualtrics-survey-definitions-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Qualtrics automations API
  slug: open-qualtrics-automations-api
- collection_type: open
  name: Qualtrics automations Directories API
  slug: open-qualtrics-directories-api
- collection_type: open
  name: Qualtrics automations Distributions API
  slug: open-qualtrics-distributions-api
- collection_type: open
  name: Qualtrics automations Eventsubscriptions API
  slug: open-qualtrics-eventsubscriptions-api
- collection_type: open
  name: Qualtrics automations file API
  slug: open-qualtrics-file-api
- collection_type: open
  name: Qualtrics automations files API
  slug: open-qualtrics-files-api
- collection_type: open
  name: Qualtrics automations Survey Definitions API
  slug: open-qualtrics-survey-definitions-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/qualtrics-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/qualtrics-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/qualtrics-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qualtrics-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qualtrics-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.qualtrics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.qualtrics.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/qualtrics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/qualtrics
- group: company
  title: ''
  type: Blog
  url: https://www.qualtrics.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.qualtrics.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qualtrics.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/Qualtrics
- group: commercial
  title: ''
  type: Plans
  url: plans/qualtrics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qualtrics-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/qualtrics-finops.yml
created: '2026-06-13'
description: Qualtrics is an experience management platform providing REST APIs for managing surveys, accessing response data, distributing surveys, managing contacts, and automating XM programs at scale. The Qualtrics v3 API enables developers to automate repetitive processes, integrate data across systems, and build custom extensions for customer, employee, product, and brand experience programs.
examples:
- key_count: 8
  name: Qualtrics Api Examples
  slug: qualtrics-api-examples
finops:
- name: Qualtrics Finops
  service_category: ''
  slug: qualtrics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qualtrics.png
json_schemas:
- name: CreateContactInMailingList
  property_count: 4
  slug: createcontactinmailinglist
- name: CreateDistributionLinks
  property_count: 6
  slug: createdistributionlinks
- name: DistributionsResponse
  property_count: 2
  slug: distributionsresponse
- name: EventSubscriptionHookSchema
  property_count: 3
  slug: eventsubscriptionhookschema
- name: EventSubscriptionsResponse
  property_count: 2
  slug: eventsubscriptionsresponse
- name: RetrieveDistributionLinksResponse
  property_count: 2
  slug: retrievedistributionlinksresponse
- name: SubscribeToEventBody
  property_count: 3
  slug: subscribetoeventbody
- name: SurveyResponse
  property_count: 1
  slug: surveyresponse
jsonld:
- class_count: 14
  name: Qualtrics Api Context
  property_count: 24
  slug: qualtrics-api-context
layout: provider
modified: '2026-06-13'
name: Qualtrics
nav: Providers
network: true
overview: 'Qualtrics publishes 7 APIs on the [APIs.io](https://apis.io/) network, including automations API, Directories API, Distributions API, and 4 more. Tagged areas include Experience Management, Surveys, Customer Experience, Employee Experience, and Market Research.


  The Qualtrics catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Qualtrics'' developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Qualtrics Plans Pricing
  plan_count: 5
  slug: qualtrics-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Qualtrics Rate Limits
  slug: qualtrics-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Qualtrics API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: qualtrics-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.3
  coverage:
    artifact_dirs: 15
    catalog_gap: 18.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 25.0
    contract_quality: 66.9
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 52.6
  previous_composite: 51.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qualtrics/refs/heads/main/screenshots/qualtrics-2026-06-20T192401.png
security:
- kind: authentication
  name: Qualtrics Authentication
  slug: qualtrics-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Qualtrics Domain Security
  slug: qualtrics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Qualtrics Vulnerability Disclosure
  slug: qualtrics-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Qualtrics Trust Center
  slug: qualtrics-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, FedRAMP, GDPR
slug: qualtrics
tags:
- Experience Management
- Surveys
- Customer Experience
- Employee Experience
- Market Research
- XM
- REST API
website: https://www.qualtrics.com/
---
