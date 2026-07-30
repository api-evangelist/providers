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
- acting_count: 9
  human_in_the_loop: 1
  name: Developerhub Agentic Access
  operation_count: 20
  slug: developerhub-agentic-access
  summary_line: 20 operations · 9 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: DeveloperHub provides a hosted platform for creating developer documentation including API references auto-generated from OpenAPI specs, user guides with a WYSIWYG editor, versioned documentation, ful
  name: DeveloperHub Documentation Platform
  slug: platform
- description: The Documentation API from DeveloperHub — 1 operation(s) for documentation.
  name: DeveloperHub Documentation API
  slug: developerhub-documentation-api
- description: The Pages API from DeveloperHub — 4 operation(s) for pages.
  name: DeveloperHub Pages API
  slug: developerhub-pages-api
- description: The Project API from DeveloperHub — 5 operation(s) for project.
  name: DeveloperHub Project API
  slug: developerhub-project-api
- description: The Reader Access API from DeveloperHub — 1 operation(s) for reader access.
  name: DeveloperHub Reader Access API
  slug: developerhub-reader-access-api
- description: The References API from DeveloperHub — 3 operation(s) for references.
  name: DeveloperHub References API
  slug: developerhub-references-api
- description: The Versions API from DeveloperHub — 2 operation(s) for versions.
  name: DeveloperHub Versions API
  slug: developerhub-versions-api
artifact_total: 15
collections:
- collection_type: open
  name: DeveloperHub.io API
  slug: open-developerhub
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/developerhub-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/developerhub-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/developerhub-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/developerhub-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/developerhub-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/developer-hub
- group: company
  title: ''
  type: Website
  url: https://developerhub.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.developerhub.io
- group: commercial
  title: ''
  type: Pricing
  url: https://developerhub.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://developerhub.io/blog
- group: start
  title: ''
  type: Login
  url: https://app.developerhub.io
- group: start
  title: ''
  type: Signup
  url: https://app.developerhub.io/signup
- group: operate
  title: ''
  type: Support
  url: https://developerhub.io/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developerhub.io/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developerhub.io/terms
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.developerhub.io/llms.txt
created: '2026-03-25'
description: DeveloperHub is a hosted developer documentation platform that enables teams to create beautiful API references, user guides, and knowledge bases. It features auto-generated API documentation from OpenAPI specifications, built-in versioning, full-text search, custom domains, and a WYSIWYG editor. DeveloperHub provides a complete developer portal solution with support for multiple documentation projects, custom branding, and SEO optimization.
finops:
- name: Developerhub Finops
  service_category: API
  slug: developerhub-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/developerhub.png
layout: provider
modified: '2026-04-28'
name: DeveloperHub
nav: Providers
network: true
overview: 'DeveloperHub publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Documentation API, Pages API, Project API, and 3 more. Tagged areas include API Reference, Developer Portals, Documentation, and Knowledge Base.


  DeveloperHub''s developer surface includes authentication, documentation, pricing, engineering blog, signup flow, support, and 10 more developer resources.'
plans:
- name: Developerhub Plans Pricing
  plan_count: 3
  slug: developerhub-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 5
  name: Developerhub Rate Limits
  slug: developerhub-rate-limits
score:
  band: developing
  composite: 45.8
  delta: -1.4
  facets:
    commercial_clarity: 84.2
    contract_quality: 53.4
    developer_ergonomics: 26.1
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 47.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/developerhub/refs/heads/main/screenshots/developerhub-2026-06-20T175947.png
security:
- kind: authentication
  name: Developerhub Authentication
  slug: developerhub-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Developerhub Domain Security
  slug: developerhub-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Developerhub Vulnerability Disclosure
  slug: developerhub-vulnerability-disclosure
  summary_line: disclosure policy published
slug: developerhub
tags:
- API Reference
- Developer Portals
- Documentation
- Knowledge Base
website: https://developerhub.io
---
