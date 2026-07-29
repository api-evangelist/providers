---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Accredible Agentic Access
  operation_count: 45
  slug: accredible-agentic-access
  summary_line: 45 operations · 32 acting
api_count: 10
apis:
- description: Issuer-level and per-credential engagement analytics.
  name: Accredible Analytics API
  slug: accredible-analytics-api
- description: Issue, retrieve, update, delete, search, and verify digital credentials.
  name: Accredible Credentials API
  slug: accredible-credentials-api
- description: Independent sub-organizations within an issuer account.
  name: Accredible Departments API
  slug: accredible-departments-api
- description: Reusable visual specifications for rendering badges and certificates.
  name: Accredible Designs API
  slug: accredible-designs-api
- description: Supplemental work samples attached to a credential.
  name: Accredible Evidence Items API
  slug: accredible-evidence-items-api
- description: Course or achievement containers that credentials are issued against.
  name: Accredible Groups API
  slug: accredible-groups-api
- description: Issuer account details and API token management.
  name: Accredible Issuer API
  slug: accredible-issuer-api
- description: Peer, teacher, or manager endorsements attached to a credential.
  name: Accredible References API
  slug: accredible-references-api
- description: Recipient single sign-on link generation.
  name: Accredible SSO API
  slug: accredible-sso-api
- description: Administrators and roles within the issuer account.
  name: Accredible Team Members API
  slug: accredible-team-members-api
artifact_total: 18
collections:
- collection_type: open
  name: Accredible API
  slug: open-accredible
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/accredible-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/accredible-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accredible-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/accredible-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/accredible-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/accredible-finops.yml
created: '2026-07-05'
description: Accredible is a digital credentialing platform for issuing, managing, and verifying digital certificates and Open Badges. The REST API lets issuers create and update credentials (certificates and badges) for recipients, organize them into Groups (courses/achievements), apply reusable visual Designs, attach Evidence Items and References, generate PDFs and blockchain-verifiable records, pull engagement analytics, manage Departments and Team Members, and generate recipient SSO links. Credentials are issued against a Group and rendered with a Design; the platform hosts a public verification page and share links for each credential.
finops:
- name: Accredible Finops
  service_category: Digital Credentialing
  slug: accredible-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/accredible.png
layout: provider
modified: '2026-07-05'
name: Accredible
nav: Providers
network: true
overview: 'Accredible publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Credentials API, Departments API, and 7 more. Tagged areas include Digital Credentials, Certificates, Badges, Open Badges, and Credentialing.


  Accredible''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Accredible Plans Pricing
  plan_count: 4
  slug: accredible-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 3
  name: Accredible Rate Limits
  slug: accredible-rate-limits
score:
  band: thin
  composite: 40.5
  delta: -2.2
  facets:
    commercial_clarity: 47.4
    contract_quality: 59.7
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 42.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/accredible/refs/heads/main/screenshots/accredible-2026-07-25T181445.png
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
