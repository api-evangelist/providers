---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Microsoft Azure Communication Services Agentic Access
  operation_count: 5
  slug: microsoft-azure-communication-services-agentic-access
  summary_line: 5 operations · 5 acting
api_count: 3
apis:
- baseURL: https://{resource}.communication.azure.com/
  baseurl_source: declared
  description: The Email API from microsoft-azure-communication-services — 1 operation(s) for email.
  name: microsoft-azure-communication-services Email API
  slug: microsoft-azure-communication-services-email-api
- baseURL: https://{resource}.communication.azure.com/
  baseurl_source: declared
  description: The Identity API from microsoft-azure-communication-services — 3 operation(s) for identity.
  name: microsoft-azure-communication-services Identity API
  slug: microsoft-azure-communication-services-identity-api
- baseURL: https://{resource}.communication.azure.com/
  baseurl_source: declared
  description: The SMS API from microsoft-azure-communication-services — 1 operation(s) for sms.
  name: microsoft-azure-communication-services SMS API
  slug: microsoft-azure-communication-services-sms-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure Communication Services REST Email API
  slug: open-microsoft-azure-communication-services-email-api
- collection_type: open
  name: Azure Communication Services REST Email Identity API
  slug: open-microsoft-azure-communication-services-identity-api
- collection_type: open
  name: Azure Communication Services REST Email SMS API
  slug: open-microsoft-azure-communication-services-sms-api
- collection_type: open
  name: Azure Communication Services REST API
  slug: open-microsoft-azure-communication-services
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-communication-services-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-communication-services-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-communication-services-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/feed/
created: '2026-03-13'
description: Azure Communication Services REST API.
finops:
- name: Microsoft Azure Communication Services Finops
  service_category: API
  slug: microsoft-azure-communication-services-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-communication-services.png
layout: provider
modified: '2026-05-19'
name: Microsoft Azure Communication Services
nav: Providers
network: true
overview: 'Microsoft Azure Communication Services publishes 3 APIs on the [APIs.io](https://apis.io/) network: microsoft-azure-communication-services Email API, microsoft-azure-communication-services Identity API, and microsoft-azure-communication-services SMS API.


  Microsoft Azure Communication Services'' developer surface includes authentication, developer portal, pricing, support, engineering blog, and 6 more developer resources.'
plans:
- name: Microsoft Azure Communication Services Plans Pricing
  plan_count: 3
  slug: microsoft-azure-communication-services-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Microsoft Azure Communication Services Rate Limits
  slug: microsoft-azure-communication-services-rate-limits
score:
  band: thin
  composite: 37.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 0.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 51.7
    developer_ergonomics: 38.1
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    note: provider declares no identity tags; regime could not be determined
    undetermined: true
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-communication-services/refs/heads/main/screenshots/microsoft-azure-communication-services-2026-06-20T185404.png
security:
- kind: authentication
  name: Microsoft Azure Communication Services Authentication
  slug: microsoft-azure-communication-services-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Microsoft Azure Communication Services Domain Security
  slug: microsoft-azure-communication-services-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-communication-services
website: https://portal.azure.com/
---
