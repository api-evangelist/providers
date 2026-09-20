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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.0
  scored_at: '2026-09-19'
api_count: 1
apis:
- description: 'Beamy''s platform surface: browser-extension usage discovery, SSO-correlated identity, application and people sheets, segments, roles and permissions, and spend and renewal intelligence across a large '
  name: Beamy SaaS Management Platform
  slug: beamy
artifact_total: 22
common:
- group: company
  title: ''
  type: Website
  url: https://beamy.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.beamy.io/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.beamy.io/en/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.beamy.io/
- group: start
  title: ''
  type: Login
  url: https://app.beamy.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://beamy.xyz/privacy-policy
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/beamy/refs/heads/main/llms/beamy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beamy-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beamy/refs/heads/main/security/beamy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beamy-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beamy/refs/heads/main/authentication/beamy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/beamy-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/beamy/refs/heads/main/lifecycle/beamy-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/beamy-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/beamy/refs/heads/main/plans/beamy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/beamy-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/beamy/refs/heads/main/rate-limits/beamy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/beamy-rate-limits.yml
coverage:
  checked: '2026-09-18'
  detail: api.beamy.io is a Kong 3.9.3 gateway answering 401 'No API key found in request' on every path, and docs.beamy.io releases implementation documentation only after a lead form (email, name, company) and the full library only to logged-in Beamy customers; beamy.xyz itself is a four-page demo-request site.
  evidence:
  - status: 401
    url: https://api.beamy.io/openapi.json
  - status: 200
    url: https://docs.beamy.io/en/articles/304306-how-to-access-beamy-s-documentation
  - status: 404
    url: https://beamy.xyz/pricing
  - status: 301
    url: https://www.beamy.io/product/
  - status: 200
    url: https://beamy.xyz
  reason: customer-only-docs
  state: gated
created: '2026-03-27'
description: 'Beamy is an enterprise application-portfolio and usage-intelligence platform from Beamy SAS (Lille and Paris, France). It began as a SaaS discovery and governance product — browser-extension detection of shadow IT, SSO and ITSM integrations, spend and license tracking, security and compliance policy — and now positions itself as an AI-driven business transformation platform: modelling people, processes and applications from real usage signals so IT, finance and transformation leaders can rationalize their stack, negotiate renewals on actual consumption, and prioritize where to deploy AI. Sold to large enterprises (Veolia, Stellantis, Decathlon, Danske Bank, Equans) through a demo-request motion; its API sits behind a key-gated Kong gateway and its implementation documentation behind a lead form.'
features:
- description: Browser extension-based discovery of all SaaS applications used across the organization, including shadow IT.
  name: SaaS Discovery
- description: Continuous monitoring to detect unauthorized applications and provide risk assessments for ungoverned SaaS.
  name: Shadow IT Monitoring
- description: Track and optimize SaaS spending across all applications with license utilization and renewal management.
  name: Spend Management
- description: Manage user access to SaaS applications throughout the employee lifecycle from onboarding to offboarding.
  name: User Lifecycle Management
- description: Assess SaaS security posture, identify risky applications, and enforce compliance with corporate policies.
  name: Security and Compliance
- description: Integration with SSO providers to correlate SaaS usage with identity management and access controls.
  name: SSO Integration
finops:
- name: Beamy Finops
  service_category: API
  slug: beamy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/beamy.png
integrations:
- description: SSO and identity integration for correlating SaaS usage with user identity and access management.
  name: Okta
- description: Microsoft Azure Active Directory integration for SaaS user provisioning and access governance.
  name: Azure AD
- description: Notification integration for alerting IT teams about new shadow IT discoveries and policy violations.
  name: Slack
- description: ITSM integration for creating and managing SaaS application requests and approvals through ServiceNow.
  name: ServiceNow
- description: Expense management integration to identify and track SaaS purchases made via employee credit cards.
  name: Expensify
layout: provider
modified: '2026-09-18'
name: Beamy
nav: Providers
network: true
overview: 'Beamy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include SaaS Management, Shadow IT, IT Asset Management, Cloud Governance, and Security.


  Beamy''s developer surface includes documentation, authentication, and 10 more developer resources.'
plans:
- name: Beamy Plans Pricing
  plan_count: 0
  slug: beamy-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Beamy Rate Limits
  slug: beamy-rate-limits
score:
  band: emerging
  composite: 18.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 25.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 75.9
    operational_transparency: 7.9
  previous_composite: 19.3
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/beamy/refs/heads/main/screenshots/beamy-2026-06-20T173122.png
security:
- kind: authentication
  name: Beamy Authentication
  slug: beamy-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Beamy Domain Security
  slug: beamy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: beamy
tags:
- SaaS Management
- Shadow IT
- IT Asset Management
- Cloud Governance
- Security
- Application Portfolio Management
- Usage Analytics
- AI Governance
use_cases:
- description: Discover and govern unauthorized cloud applications used by employees outside IT approval processes.
  name: Shadow IT Elimination
- description: Identify unused licenses, duplicate tools, and overspending to reduce overall SaaS costs.
  name: SaaS Cost Optimization
- description: Assess and mitigate security risks from unapproved or high-risk SaaS applications.
  name: Security Risk Reduction
- description: Generate compliance reports showing which applications are approved, their data handling policies, and user access.
  name: Compliance Reporting
- description: Centralize SaaS vendor relationships, contract renewals, and negotiation data in one platform.
  name: Vendor Management
website: https://beamy.xyz
---
