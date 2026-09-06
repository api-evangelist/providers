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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.6
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: 'The CloudEagle API is an enterprise REST surface that exposes the same SaaS-management primitives as the web app: discovered applications, licenses and usage, identity and access state, onboarding/off'
  name: CloudEagle API
  slug: cloudeagle-api
- description: A live, OAuth-protected Model Context Protocol server CloudEagle serves from its own hostname mcp.cloudeagle.ai, letting IT, security, finance and procurement teams query their live SaaS, AI-applicati
  name: CloudEagle.ai MCP Server
  slug: cloudeagle-mcp
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudeagle-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloudeagle
- group: company
  title: ''
  type: Website
  url: https://www.cloudeagle.ai/
- group: other
  title: ''
  type: Resources
  url: https://www.cloudeagle.ai/resources/guides-and-reports
- group: other
  title: ''
  type: SaaSManagement
  url: https://www.cloudeagle.ai/product/saas-management
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cloudeagle.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cloudeagle.ai/terms-and-conditions
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cloudeagle.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.cloudeagle.ai/blogs
- group: operate
  title: ''
  type: Support
  url: https://www.cloudeagle.ai/contact
- group: start
  title: ''
  type: SignUp
  url: https://www.cloudeagle.ai/free-trial
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cloudeagle.ai/how-it-works
- group: auth
  title: ''
  type: Compliance
  url: https://www.cloudeagle.ai/compliance/soc-2
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cloudeagle-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cloudeagle-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cloudeagle-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudeagle-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cloudeagle-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cloudeagle-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cloudeagle-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cloudeagle-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cloudeagle-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/cloudeagle-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cloudeagle-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cloudeagle-rate-limits.yml
created: '2026-03-16'
description: CloudEagle.ai is an AI-powered SaaS management, procurement and identity governance platform that helps IT, security, finance and procurement teams discover, govern, optimize and renew their SaaS and AI application portfolio. It offers application discovery via 500+ integrations with SSO, HRIS, finance and CASB systems; license harvesting and spend optimization; access governance with automated access reviews; onboarding/offboarding automation; procurement and renewal orchestration; and shadow IT/shadow AI detection. CloudEagle exposes an enterprise API at api.cloudeagle.ai whose endpoints and credentials are provisioned to customers in-product rather than on a public docs site, and it operates a live OAuth-protected Model Context Protocol server at mcp.cloudeagle.ai that lets teams query their SaaS, AI, licence, contract and identity data from Claude, ChatGPT, Gemini or Copilot. That MCP server is the only machine-readable surface CloudEagle publishes.
finops:
- name: Cloudeagle Finops
  service_category: API
  slug: cloudeagle-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudeagle.png
layout: provider
mcp_servers:
- description: A live, OAuth-protected Model Context Protocol server served from CloudEagle's own hostname mcp.cloudeagle.ai. CloudEagle announced it publicly as a way for IT, Security, Finance and Procurement teams
  name: CloudEagle.ai MCP Server
  slug: cloudeagleai-mcp-server
modified: '2026-09-05'
name: CloudEagle.ai
nav: Providers
network: true
overview: 'CloudEagle.ai publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Access Governance, Cost Optimization, License Management, Procurement, and SaaS Management.


  CloudEagle.ai''s developer surface includes pricing, engineering blog, support, signup flow, getting-started guide, authentication, changelog, and 18 more developer resources.'
plans:
- name: Cloudeagle Plans Pricing
  plan_count: 0
  slug: cloudeagle-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Cloudeagle Rate Limits
  slug: cloudeagle-rate-limits
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 17.8
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 15.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudeagle/refs/heads/main/screenshots/cloudeagle-2026-06-20T174549.png
security:
- kind: authentication
  name: Cloudeagle Authentication
  slug: cloudeagle-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Cloudeagle Domain Security
  slug: cloudeagle-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cloudeagle
tags:
- Access Governance
- Cost Optimization
- License Management
- Procurement
- SaaS Management
- Shadow AI
- Shadow IT
- Software Procurement
- Vendor Management
website: https://www.cloudeagle.ai/
---
