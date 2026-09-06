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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 334
  human_in_the_loop: 18
  name: Ovh Cloud Agentic Access
  operation_count: 716
  slug: ovh-cloud-agentic-access
  summary_line: 716 operations · 334 acting · 18 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.us.ovhcloud.com/v1
  baseurl_source: declared
  description: The Cloud API from OVH Cloud — 469 operation(s) for cloud.
  name: OVH Cloud Cloud API
  slug: ovh-cloud-cloud-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OVH OVHcloud API specification Cloud API
  slug: open-ovh-cloud-cloud-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ovh-cloud-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ovh-cloud-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ovh-cloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ovh-cloud-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ovh-cloud-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ovh
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ovhgroup
- group: other
  title: ''
  type: Developer
  url: https://api.us.ovhcloud.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.us.ovhcloud.com/
- group: company
  title: ''
  type: Blog
  url: https://us.ovhcloud.com/resources/blog/
- group: operate
  title: ''
  type: Support
  url: https://us.ovhcloud.com/support/
- group: other
  title: ''
  type: CaseStudies
  url: https://us.ovhcloud.com/resources/case-studies/
- group: learn
  title: ''
  type: Videos
  url: https://us.ovhcloud.com/videos/
- group: learn
  title: ''
  type: Tutorials
  url: https://us.ovhcloud.com/community/tutorials/
- group: other
  title: ''
  type: WhitePapers
  url: https://us.ovhcloud.com/resources/white-papers/
- group: other
  title: ''
  type: Glossary
  url: https://us.ovhcloud.com/glossary/
- group: start
  title: ''
  type: Login
  url: https://us.ovhcloud.com/auth/
- group: start
  title: ''
  type: Signup
  url: https://us.ovhcloud.com/auth/
- group: company
  title: ''
  type: Website
  url: https://us.ovhcloud.com/
- group: company
  title: ''
  type: About
  url: https://us.ovhcloud.com/about/
- group: operate
  title: ''
  type: PressReleases
  url: https://us.ovhcloud.com/press/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://us.ovhcloud.com/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://us.ovhcloud.com/legal/privacy-policy/
created: '2024-04-18'
description: OVH Cloud is a leading provider of cloud computing services that offer a wide range of solutions for businesses of all sizes. From virtual private servers and dedicated servers to storage, networking, and security services, OVH Cloud provides a comprehensive platform for organizations to build and deploy their applications and services in the cloud. With data centers located around the world, OVH Cloud offers high availability, scalability, and flexibility to meet the needs of its customers.
finops:
- name: Ovh Cloud Finops
  service_category: API
  slug: ovh-cloud-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ovh-cloud.png
layout: provider
modified: '2026-05-19'
name: OVH Cloud
nav: Providers
network: true
overview: 'OVH Cloud publishes 1 API on the [APIs.io](https://apis.io/) network: Cloud API. Tagged areas include Cloud, Compute, Servers, and Hosting.


  OVH Cloud''s developer surface includes authentication, engineering blog, support, signup flow, and 19 more developer resources.'
plans:
- name: Ovh Cloud Plans Pricing
  plan_count: 3
  slug: ovh-cloud-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Ovh Cloud Rate Limits
  slug: ovh-cloud-rate-limits
scopes:
- name: Ovh Cloud Scopes
  scope_count: 3
  slug: ovh-cloud-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 49.7
    developer_ergonomics: 35.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 38.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ovh-cloud/refs/heads/main/screenshots/ovh-cloud-2026-06-20T191242.png
security:
- kind: authentication
  name: Ovh Cloud Authentication
  slug: ovh-cloud-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Ovh Cloud Domain Security
  slug: ovh-cloud-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Ovh Cloud Vulnerability Disclosure
  slug: ovh-cloud-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ovh-cloud
tags:
- Cloud
- Compute
- Servers
- Hosting
website: https://us.ovhcloud.com/
---
