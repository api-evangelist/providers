---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 27.2
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The PixieBrix Developer API is the token-authenticated REST admin and package-registry API for PixieBrix teams. It covers organization and group management, memberships and invitations, service accoun
  name: PixieBrix Developer API
  slug: pixiebrix-developer-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.pixiebrix.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.pixiebrix.com/developer-api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pixiebrix.com/
- group: docs
  title: ''
  type: APIReference
  url: https://app.pixiebrix.com/api/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pixiebrix.com/developer-api/making-an-api-request
- group: start
  title: ''
  type: SignUp
  url: https://app.pixiebrix.com/login/
- group: start
  title: ''
  type: Login
  url: https://app.pixiebrix.com/login/
- group: operate
  title: ''
  type: Support
  url: https://www.pixiebrix.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.pixiebrix.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pixiebrix.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pixiebrix.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pixiebrix.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pixiebrix
- group: operate
  title: ''
  type: StatusPage
  url: https://pixiebrix.statuspage.io/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.pixiebrix.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.pixiebrix.com/security
- group: auth
  title: ''
  type: Security
  url: security/pixiebrix-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pixiebrix-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pixiebrix-domain-security.yml
- group: other
  title: ''
  type: Marketplace
  url: https://www.pixiebrix.com/marketplace
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pixiebrix-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pixiebrix-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pixiebrix-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.pixiebrix.com/developer-api/deprecated-resources
- group: build
  title: ''
  type: Packages
  url: packages/pixiebrix-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pixiebrix-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pixiebrix-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pixiebrix-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/pixiebrix-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-26'
description: PixieBrix is a browser-based platform for customer care and enterprise operations teams that layers automation, AI assistance, integrations and real-time policy enforcement onto the web applications a team already uses, deployed as a lightweight browser extension and companion web app rather than an endpoint agent. Teams build "mods" from a library of prebuilt "bricks" — DOM readers, UI components, HTTP request bricks, AI/LLM bricks and data connectors — and administrators govern them centrally through activity policies, deployments, groups and audit trails. The public PixieBrix Developer API is a token-authenticated REST surface at https://app.pixiebrix.com/api/ covering team management, package/registry publishing, deployments, databases, activity policy and health checks, described by a published OpenAPI 3.0.2 specification.
image: https://cdn.prod.website-files.com/627def74bc73d85070c65929/697cf1b5cee0b7370cdc763a_pixiebrixog.png
layout: provider
modified: '2026-08-26'
name: PixieBrix
nav: Providers
network: true
overview: 'PixieBrix publishes 1 API on the [APIs.io](https://apis.io/) network: Developer API. Tagged areas include Company, Browser Extensions, Low-Code, Automation, and Artificial Intelligence.


  PixieBrix''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, pricing, and 23 more developer resources.'
plans:
- name: Pixiebrix Plans Pricing
  plan_count: 4
  slug: pixiebrix-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Pixiebrix Rate Limits
  slug: pixiebrix-rate-limits
score:
  band: strong
  composite: 61.9
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 30.3
    contract_quality: 44.1
    developer_ergonomics: 66.1
    discoverability: 87.0
    governance: 30.3
    operational_transparency: 73.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Pixiebrix Authentication
  slug: pixiebrix-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Pixiebrix Domain Security
  slug: pixiebrix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pixiebrix Vulnerability Disclosure
  slug: pixiebrix-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Pixiebrix Trust Center
  slug: pixiebrix-trust-center
  summary_line: SOC 2, PCI DSS, GDPR
slug: pixiebrix
tags:
- Company
- Browser Extensions
- Low-Code
- Automation
- Artificial Intelligence
- Customer Support
- Enterprise Operations
- Workflow Automation
- Agent Governance
- Robotic Process Automation
website: https://www.pixiebrix.com/
---
