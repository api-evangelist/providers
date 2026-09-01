---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: Enterprise API for retrieving finalized Stensul email content and distributing it to any platform in a customer's ecosystem, removing the manual export step between Stensul and the downstream ESP/MAP.
  name: Stensul Content API
  slug: stensul-content-api
- description: 'Enterprise API for automating the provisioning, management and de-provisioning of Stensul users and their roles and permissions. Stensul''s public integration page states it supports SCIM provisioning '
  name: Stensul User API
  slug: stensul-user-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/stensul-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://stensul.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stensul
- group: docs
  title: ''
  type: Documentation
  url: https://helpdesk.stensul.com/en/
- group: operate
  title: ''
  type: Support
  url: https://helpdesk.stensul.com/en/
- group: company
  title: ''
  type: Blog
  url: https://stensul.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://stensul.com/feed/
- group: commercial
  title: ''
  type: Pricing
  url: https://stensul.com/stensul-pricing-request/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://stensul.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.stensul.com/
- group: auth
  title: ''
  type: Compliance
  url: https://stensul.com/security-trust-center/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stensul-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stensul-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/stensul-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stensul-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/stensul-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/stensul-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stensul-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/stensul-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stensul-rate-limits.yml
coverage:
  checked: '2026-08-29'
  detail: 'Stensul markets two named enterprise APIs on https://stensul.com/our-integrations/api-endpoints/ — a Content API and a User API — but every route from those pages ends at "Request a demo": there is no developer portal, no api./docs./developer. subdomain (all three fail DNS resolution), no API reference in the public Intercom help center, which exposes exactly one collection ("Integrations"), and no base URL, endpoint, scope or error published anywhere a machine can read.'
  evidence:
  - status: 200
    url: https://stensul.com/our-integrations/api-endpoints/
  - status: 200
    url: https://stensul.com/integrations/stensul-content-api/
  - status: 200
    url: https://stensul.com/integrations/stensul-user-api/
  - status: 0
    url: https://docs.stensul.com/
  - status: 0
    url: https://developer.stensul.com/
  - status: 0
    url: https://api.stensul.com/
  - status: 200
    url: https://helpdesk.stensul.com/en/
  reason: sales-gate
  state: gated
created: '2026-08-29'
description: Stensul is an enterprise email and landing page creation platform — it calls the category "Governed Creation" — used by large marketing organizations to build, review, approve and deploy campaign assets without hand-coding HTML for every send. Marketers assemble emails and landing pages from brand-locked, developer-built modules; the platform runs the review and approval workflow, then pushes the finished asset into the ESP or marketing automation platform of record (Salesforce Marketing Cloud, Marketo, Adobe Campaign, Adobe Journey Optimizer, Oracle Eloqua, Braze, Iterable, Acoustic, Responsys, Epsilon PeopleCloud, Zeta and others). Stensul markets two enterprise APIs — a Content API for retrieving and distributing finished email content to any downstream system, and a User API for automating user provisioning and de-provisioning — both described as using OAuth server-to-server authentication with IP address allowlisting, with the User API additionally claiming support for
  SCIM provisioning standards. Neither API has a public reference, base URL, or machine-readable specification published on stensul.com; the endpoint pages are marketing descriptions that route to a sales conversation. The company was founded in 2015 and is headquartered in New York.
image: https://stensul.com/wp-content/uploads/2025/10/Stensul-Logomark-Black-RGB.svg
layout: provider
modified: '2026-08-29'
name: Stensul
nav: Providers
network: true
overview: 'Stensul publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Email, Email Marketing, Marketing, and Marketing Automation.


  Stensul''s developer surface includes documentation, support, engineering blog, pricing, authentication, and 15 more developer resources.'
plans:
- name: Stensul Plans Pricing
  plan_count: 0
  slug: stensul-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Stensul Rate Limits
  slug: stensul-rate-limits
score:
  band: emerging
  composite: 24.3
  coverage:
    artifact_dirs: 12
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 24.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Stensul Authentication
  slug: stensul-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Stensul Domain Security
  slug: stensul-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Stensul Vulnerability Disclosure
  slug: stensul-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Stensul Trust Center
  slug: stensul-trust-center
  summary_line: SOC 2 Type 2
slug: stensul
tags:
- Company
- Email
- Email Marketing
- Marketing
- Marketing Automation
- Content Management
- Landing Pages
- Marketing Operations
- Enterprise Software
- Governance
- Collaboration
- Software-as-a-Service
website: https://stensul.com/
---
