---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Accredible Agentic Access
  operation_count: 45
  slug: accredible-agentic-access
  summary_line: 45 operations · 29 acting
api_count: 1
apis:
- baseURL: https://api.accredible.com/v1
  baseurl_source: declared
  description: Issuer-level and per-credential engagement analytics.
  name: Accredible Analytics API
  slug: accredible-analytics-api
- baseURL: https://api.accredible.com/v1
  baseurl_source: declared
  description: Issue, retrieve, update, delete, search, and verify digital credentials.
  name: Accredible Credentials API
  slug: accredible-credentials-api
- baseURL: https://api.accredible.com/v1
  baseurl_source: declared
  description: Independent sub-organizations within an issuer account.
  name: Accredible Departments API
  slug: accredible-departments-api
- baseURL: https://api.accredible.com/v1
  baseurl_source: declared
  description: Reusable visual specifications for rendering badges and certificates.
  name: Accredible Designs API
  slug: accredible-designs-api
- baseURL: https://api.accredible.com/v1
  baseurl_source: declared
  description: Supplemental work samples attached to a credential.
  name: Accredible Evidence Items API
  slug: accredible-evidence-items-api
- baseURL: https://api.accredible.com/v1
  baseurl_source: declared
  description: Course or achievement containers that credentials are issued against.
  name: Accredible Groups API
  slug: accredible-groups-api
- baseURL: https://api.accredible.com/v1
  baseurl_source: declared
  description: Peer, teacher, or manager endorsements attached to a credential.
  name: Accredible References API
  slug: accredible-references-api
- baseURL: https://api.accredible.com/v1
  baseurl_source: declared
  description: Recipient single sign-on link generation.
  name: Accredible SSO API
  slug: accredible-sso-api
- baseURL: https://api.accredible.com/v1
  baseurl_source: declared
  description: Administrators and roles within the issuer account.
  name: Accredible Team Members API
  slug: accredible-team-members-api
- baseURL: https://api.accredible.com/v1
  baseurl_source: declared
  description: 'Attributes provide a way to add information to certificates/emails. A full guide on Attributes can be found here: https://help.accredible.com/a-quick-guide-to-attributes'
  name: Accredible Attributes API
  slug: accredible-attributes-api
- baseURL: https://api.accredible.com/v1
  baseurl_source: declared
  description: A Collection is a curated set of groups. To create one, you'll need to provide a collection name, a description, and indicate whether it should be public or private. Once created, you can assign group
  name: Accredible Collections API
  slug: accredible-collections-api
- baseURL: https://api.accredible.com/v1
  baseurl_source: declared
  description: The following endpoints require the `data_exports` feature to be switched on, which is based on your pricing plan.
  name: Accredible Data Exports API
  slug: accredible-data-exports-api
- baseURL: https://api.accredible.com/v1
  baseurl_source: declared
  description: The Issuers API from Accredible — 1 operation(s) for issuers.
  name: Accredible Issuers API
  slug: accredible-issuers-api
- baseURL: https://api.accredible.com/v1
  baseurl_source: declared
  description: A Skills Framework is a structured taxonomy of skills. Accredible maintains external frameworks such as O*NET, ESCO and NACE, and your organization can upload its own custom frameworks. Tagging a Grou
  name: Accredible Skills Frameworks API
  slug: accredible-skills-frameworks-api
artifact_total: 33
collections:
- collection_type: open
  name: Accredible Analytics API
  slug: open-accredible-analytics-api
- collection_type: open
  name: Accredible Analytics Credentials API
  slug: open-accredible-credentials-api
- collection_type: open
  name: Accredible Analytics Departments API
  slug: open-accredible-departments-api
- collection_type: open
  name: Accredible Analytics Designs API
  slug: open-accredible-designs-api
- collection_type: open
  name: Accredible Analytics Evidence Items API
  slug: open-accredible-evidence-items-api
- collection_type: open
  name: Accredible Analytics Groups API
  slug: open-accredible-groups-api
- collection_type: open
  name: Accredible Analytics Issuer API
  slug: open-accredible-issuer-api
- collection_type: open
  name: Accredible Analytics References API
  slug: open-accredible-references-api
- collection_type: open
  name: Accredible Analytics SSO API
  slug: open-accredible-sso-api
- collection_type: open
  name: Accredible Analytics Team Members API
  slug: open-accredible-team-members-api
- collection_type: open
  name: Accredible API
  slug: open-accredible
common:
- group: company
  title: ''
  type: Blog
  url: https://www.accredible.com/blog
- group: agent
  href: https://artifacts.apis.io/accredible/agentic-access/accredible-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/accredible-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/accredible/security/accredible-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/accredible-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/accredible/security/accredible-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/accredible-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/accredible/authentication/accredible-authentication.yml
  title: ''
  type: Authentication
  url: authentication/accredible-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/accredible
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/accredible
- group: company
  title: ''
  type: Website
  url: https://www.accredible.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.accredible.com/
- group: commercial
  href: https://artifacts.apis.io/accredible/plans/accredible-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/accredible-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/accredible/rate-limits/accredible-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/accredible-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/accredible/finops/accredible-finops.yml
  title: ''
  type: FinOps
  url: finops/accredible-finops.yml
created: '2026-07-05'
description: Accredible is a digital credentialing platform for issuing, managing, and verifying digital certificates and Open Badges. The REST API lets issuers create and update credentials (certificates and badges) for recipients, organize them into Groups (courses/achievements), apply reusable visual Designs, attach Evidence Items and References, generate PDFs and blockchain-verifiable records, pull engagement analytics, manage Departments and Team Members, and generate recipient SSO links. Credentials are issued against a Group and rendered with a Design; the platform hosts a public verification page and share links for each credential.
finops:
- has_sources: true
  method: generated
  name: Accredible Finops
  primary_unit: ''
  service_category: Digital Credentialing
  slug: accredible-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/accredible.png
layout: provider
modified: '2026-10-06'
name: Accredible
nav: Providers
network: true
overview: 'Accredible publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, Credentials API, Departments API, and 11 more. Tagged areas include Digital Credentials, Certificates, Badges, Open Badges, and Credentialing.


  The Accredible catalog on APIs.io includes 1 Spectral governance ruleset.


  Accredible''s developer surface includes engineering blog, authentication, documentation, and 9 more developer resources.'
plans:
- name: Accredible Plans Pricing
  plan_count: 4
  slug: accredible-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 3
  name: Accredible Rate Limits
  slug: accredible-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Accredible API Rules
  rule_count: 55
  severity_counts:
    error: 45
    hint: 0
    info: 3
    warn: 7
  slug: accredible-rules
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 50.5
    developer_ergonomics: 15.5
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 27.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 56.0
      total: 25
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/accredible/accredible-2026-07-25T181445.png
security:
- kind: authentication
  name: Accredible Authentication
  slug: accredible-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Accredible Domain Security
  slug: accredible-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Accredible Trust Center
  slug: accredible-trust-center
  summary_line: SOC 2, GDPR
slug: accredible
tags:
- Digital Credentials
- Certificates
- Badges
- Open Badges
- Credentialing
- Verification
- Digital Badges
website: https://www.accredible.com
---
