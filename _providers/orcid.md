---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Orcid Agentic Access
  operation_count: 16
  slug: orcid-agentic-access
  summary_line: 16 operations
api_count: 16
apis:
- description: The ORCID Member API allows member organizations to read, write, and update data on ORCID records with user permission.
  name: ORCID Member API
  slug: orcid-member-api
- description: The Address API from ORCID — 1 operation(s) for address.
  name: ORCID Address API
  slug: orcid-address-api
- description: The Educations API from ORCID — 1 operation(s) for educations.
  name: ORCID Educations API
  slug: orcid-educations-api
- description: The Email API from ORCID — 1 operation(s) for email.
  name: ORCID Email API
  slug: orcid-email-api
- description: The Employments API from ORCID — 1 operation(s) for employments.
  name: ORCID Employments API
  slug: orcid-employments-api
- description: The External Identifiers API from ORCID — 1 operation(s) for external identifiers.
  name: ORCID External Identifiers API
  slug: orcid-external-identifiers-api
- description: The Fundings API from ORCID — 1 operation(s) for fundings.
  name: ORCID Fundings API
  slug: orcid-fundings-api
- description: The Keywords API from ORCID — 1 operation(s) for keywords.
  name: ORCID Keywords API
  slug: orcid-keywords-api
- description: The Other Names API from ORCID — 1 operation(s) for other names.
  name: ORCID Other Names API
  slug: orcid-other-names-api
- description: The Peer Reviews API from ORCID — 1 operation(s) for peer reviews.
  name: ORCID Peer Reviews API
  slug: orcid-peer-reviews-api
- description: The Person API from ORCID — 1 operation(s) for person.
  name: ORCID Person API
  slug: orcid-person-api
- description: The Personal Details API from ORCID — 1 operation(s) for personal details.
  name: ORCID Personal Details API
  slug: orcid-personal-details-api
- description: The Record API from ORCID — 1 operation(s) for record.
  name: ORCID Record API
  slug: orcid-record-api
- description: The Researcher Urls API from ORCID — 1 operation(s) for researcher urls.
  name: ORCID Researcher Urls API
  slug: orcid-researcher-urls-api
- description: The Summary API from ORCID — 1 operation(s) for summary.
  name: ORCID Summary API
  slug: orcid-summary-api
- description: The Works API from ORCID — 2 operation(s) for works.
  name: ORCID Works API
  slug: orcid-works-api
artifact_total: 22
collections:
- collection_type: open
  name: ORCID Public API
  slug: open-orcid
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/orcid-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orcid-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/orcid
- group: start
  title: ''
  type: Portal
  url: https://orcid.org/
- group: docs
  title: ''
  type: Documentation
  url: https://info.orcid.org/documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://info.orcid.org/documentation/api-tutorials/
- group: auth
  title: ''
  type: Authentication
  url: https://info.orcid.org/documentation/api-tutorials/api-tutorial-get-and-authenticated-orcid-id/
- group: start
  title: ''
  type: Signup
  url: https://orcid.org/register
- group: start
  title: ''
  type: Login
  url: https://orcid.org/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://info.orcid.org/terms-and-conditions-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://info.orcid.org/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://support.orcid.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ORCID
- group: company
  title: ''
  type: Website
  url: https://orcid.org/
created: '2025-02-06'
description: ORCID provides a persistent digital identifier (an ORCID iD) that you own and control, and that distinguishes you from every other researcher. ORCID provides a public API for reading data from ORCID records and a member API for creating and updating records.
finops:
- name: Orcid Finops
  service_category: API
  slug: orcid-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/orcid.png
layout: provider
modified: '2026-05-19'
name: ORCID
nav: Providers
network: true
overview: 'ORCID publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Address API, Educations API, Email API, and 12 more. Tagged areas include Academic, Identity, and Researchers.


  ORCID''s developer surface includes developer portal, documentation, getting-started guide, authentication, signup flow, support, and 8 more developer resources.'
plans:
- name: Orcid Plans Pricing
  plan_count: 3
  slug: orcid-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 5
  name: Orcid Rate Limits
  slug: orcid-rate-limits
score:
  band: thin
  composite: 38.6
  delta: -8.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 47.0
    developer_ergonomics: 43.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 46.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/orcid/refs/heads/main/screenshots/orcid-2026-06-20T191203.png
security:
- kind: domain-security
  name: Orcid Domain Security
  slug: orcid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: orcid
tags:
- Academic
- Identity
- Researchers
website: https://orcid.org/
---
