---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.2
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 6
  human_in_the_loop: 6
  name: Growthspace Agentic Access
  operation_count: 12
  slug: growthspace-agentic-access
  summary_line: 12 operations · 6 acting · 6 human-in-the-loop
api_count: 1
apis:
- description: The management surface for the Growthspace Public API. It lists the scope catalogue, creates and revokes Public API applications for a company, issues bearer tokens for an application, updates an appl
  name: Growthspace Public API Management
  slug: growthspace-public-api-management
artifact_total: 7
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/growthspace-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/growthspace-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.growthspace.com/
- group: start
  title: ''
  type: Login
  url: https://app.growthspace.com/
- group: company
  title: ''
  type: Blog
  url: https://www.growthspace.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.growthspace.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.growthspace.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.growthspace.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/growthspace-engineering
- group: operate
  title: ''
  type: StatusPage
  url: https://status.growthspace.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.growthspace.com/about
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/growthspaceus/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Growthspaceus
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/growthspace-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/growthspace-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/growthspace-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/growthspace-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/growthspace-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/growthspace-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/growthspace-packages.yml
- group: design
  title: ''
  type: Components
  url: components/growthspace-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/growthspace-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/growthspace-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/growthspace-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/growthspace-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-22'
description: Growthspace is a precision skill development platform for enterprise learning and talent teams. Using AI-driven matching it pairs individual employees and cohorts with a network of more than 2,800 vetted domain experts across 65+ countries and 80+ skill sets, then runs and measures the resulting development sprints — 1:1 skill development, group skill development, workshops, internal and external mentoring, and the ExpertX on-demand expert surface. The platform handles skill-gap assessment, program execution, scheduling, and outcome measurement in one place, with native integrations into HRIS systems, Microsoft Viva Learning, Slack, Zoom and Teams. Growthspace runs a Public API whose OAuth-style applications, scopes and tokens are provisioned from the admin console; the scope catalogue covers programs, participants, workshops, company, reporting and integration surfaces in read and write variants. Headquartered in New York with customers including Siemens, Microsoft, EY and
  Johnson & Johnson.
image: https://cdn.prod.website-files.com/685bf37fcc056cf0bb7be4d1/68d6feb8a89f53402a0a9c26_Frame%20626177.avif
layout: provider
modified: '2026-08-22'
name: GrowthSpace
nav: Providers
network: true
overview: 'GrowthSpace publishes 1 API on the [APIs.io](https://apis.io/) network: Public API Management. Tagged areas include Company, Learning and Development, Talent Development, Human Resources, and Coaching.


  GrowthSpace''s developer surface includes engineering blog, support, YouTube channel, authentication, and 22 more developer resources.'
plans:
- name: Growthspace Plans Pricing
  plan_count: 0
  slug: growthspace-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Growthspace Rate Limits
  slug: growthspace-rate-limits
scopes:
- name: Growthspace Scopes
  scope_count: 11
  slug: growthspace-scopes
  summary_line: 11 scopes
score:
  band: thin
  composite: 31.4
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 30.3
    contract_quality: 30.1
    developer_ergonomics: 26.2
    discoverability: 75.9
    governance: 30.3
    operational_transparency: 2.6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
security:
- kind: authentication
  name: Growthspace Authentication
  slug: growthspace-authentication
  summary_line: bearer-token/client-credentials · 1 scheme
- kind: domain-security
  name: Growthspace Domain Security
  slug: growthspace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: growthspace
tags:
- Company
- Learning and Development
- Talent Development
- Human Resources
- Coaching
- Employee Experience
- Skills
- Workforce
- Enterprise Software
- Artificial Intelligence
website: https://www.growthspace.com/
---
