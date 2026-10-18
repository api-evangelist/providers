---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.0
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Recruitee Agentic Access
  operation_count: 31
  slug: recruitee-agentic-access
  summary_line: 31 operations · 18 acting
api_count: 10
apis:
- description: REST API for admin-side ATS operations including candidates, offers (job openings), placements, departments, requisitions, tags, evaluations, scheduled interviews, mailbox messages, and reports. All e
  name: Recruitee Company (ATS) API
  slug: company-api
- description: Public, read-only API used by careers sites and embedded job widgets to fetch published offers, departments, and locations for unauthenticated job seekers. Backs the careers.recruitee.com hosted pages
  name: Recruitee Careers Site API
  slug: careers-site-api
- description: Subscribe to ATS events such as candidate created, candidate stage changed, offer published, evaluation created, and interview scheduled to drive event-driven integrations and HRIS synchronization.
  name: Recruitee Webhooks
  slug: webhooks
- baseURL: https://api.recruitee.com/c/{company_id}
  baseurl_source: declared
  description: The C API from Recruitee — 11 operation(s) for c.
  name: Recruitee C API
  slug: recruitee-c-api
- baseURL: https://api.recruitee.com/c/{company_id}
  baseurl_source: declared
  description: The I API from Recruitee — 2 operation(s) for i.
  name: Recruitee I API
  slug: recruitee-i-api
- baseURL: https://api.recruitee.com/c/{company_id}
  baseurl_source: declared
  description: The Offers API from Recruitee — 3 operation(s) for offers.
  name: Recruitee Offers API
  slug: recruitee-offers-api
- baseURL: https://api.recruitee.com/c/{company_id}
  baseurl_source: declared
  description: The P API from Recruitee — 5 operation(s) for p.
  name: Recruitee P API
  slug: recruitee-p-api
artifact_total: 13
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/recruitee/refs/heads/main/agentic-access/recruitee-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/recruitee-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/recruitee/refs/heads/main/rules/recruitee-rules.yml
  title: ''
  type: Spectral
  url: rules/recruitee-rules.yml
- group: auth
  title: ''
  type: Compliance
  url: https://recruitee.com/compliance
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/recruitee/refs/heads/main/errors/recruitee-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/recruitee-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/recruitee/refs/heads/main/conformance/recruitee-conformance.yml
  title: ''
  type: Conformance
  url: conformance/recruitee-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/recruitee/refs/heads/main/llms/recruitee-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/recruitee-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/recruitee/refs/heads/main/well-known/recruitee-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/recruitee-support-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/recruitee/refs/heads/main/well-known/recruitee-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/recruitee-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/recruitee/refs/heads/main/well-known/recruitee-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/recruitee-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/recruitee/refs/heads/main/hosts/recruitee-hosts.yml
  title: ''
  type: Hosts
  url: hosts/recruitee-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/recruitee/refs/heads/main/integrations/recruitee-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/recruitee-integration-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/recruitee/refs/heads/main/vendors/recruitee-vendors.yml
  title: ''
  type: Vendors
  url: vendors/recruitee-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/recruitee/refs/heads/main/packages/recruitee-packages.yml
  title: ''
  type: SDKs
  url: packages/recruitee-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/recruitee/refs/heads/main/packages/recruitee-packages.yml
  title: ''
  type: Packages
  url: packages/recruitee-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://recruitee.com/terms
- group: operate
  title: ''
  type: Support
  url: https://support.recruitee.com/en
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://recruitee.com/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/recruitee/refs/heads/main/scopes/recruitee-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/recruitee-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/recruitee/refs/heads/main/authentication/recruitee-authentication.yml
  title: ''
  type: Authentication
  url: authentication/recruitee-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/recruitee/refs/heads/main/security/recruitee-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/recruitee-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/recruitee/refs/heads/main/security/recruitee-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/recruitee-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/recruitee
- group: company
  title: ''
  type: Website
  url: https://recruitee.com
- group: other
  title: ''
  type: Parent Company
  url: https://tellent.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.recruitee.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.recruitee.com/reference/getting-started
- group: operate
  title: ''
  type: Help Center
  url: https://support.recruitee.com
- group: commercial
  title: ''
  type: Pricing
  url: https://recruitee.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.recruitee.com/#/signup
- group: operate
  title: ''
  type: StatusPage
  url: https://status.recruitee.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/recruitee
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.recruitee.com/llms.txt
created: '2026-05-11'
description: Recruitee (part of Tellent) is a collaborative applicant tracking system (ATS) and recruiting platform that helps growing companies build hiring pipelines, publish careers sites, manage candidates, schedule interviews, and collaborate on hiring decisions. Its REST API at https://api.recruitee.com exposes endpoints for candidates, offers, placements, departments, tags, evaluations, interviews, mailboxes, and reports, scoped to a company by the path segment /c/{company_id}. Authentication uses a Bearer personal API token generated from Settings, Apps and plugins, Personal API tokens, with permissions inherited from the creator's Hiring role.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/recruitee.png
layout: provider
modified: '2026-05-11'
name: Recruitee
nav: Providers
network: true
overview: 'Recruitee publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including C API, I API, Offers API, and 4 more. Tagged areas include Recruiting, Applicant Tracking, Human Resources, Hiring, and Careers Site.


  The Recruitee catalog on APIs.io includes 1 Spectral governance ruleset.


  Recruitee''s developer surface includes support, authentication, documentation, API reference, pricing, signup flow, and 26 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Recruitee API Rules
  rule_count: 10
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 4
  slug: recruitee-rules
scopes:
- name: Recruitee Scopes
  scope_count: 0
  slug: recruitee-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 23.2
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 44.7
    developer_ergonomics: 32.1
    discoverability: 78.6
    operational_transparency: 18.4
  previous_composite: 21.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 75.0
      derived: 0
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 39.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/recruitee/refs/heads/main/screenshots/recruitee-2026-06-20T192710.png
security:
- kind: authentication
  name: Recruitee Authentication
  slug: recruitee-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Recruitee Domain Security
  slug: recruitee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Recruitee Trust Center
  slug: recruitee-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: recruitee
tags:
- Recruiting
- Applicant Tracking
- Human Resources
- Hiring
- Careers Site
- Tellent
website: https://recruitee.com
---
