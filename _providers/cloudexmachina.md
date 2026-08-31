---
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
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/cloudexmachina-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudexmachina-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cloudexmachina.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cloudexmachina.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cloudexmachina.io/#getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.cloudexmachina.io/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.cloudexmachina.io/blog/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cxmlabs/
- group: start
  title: ''
  type: Login
  url: https://app.cloudexmachina.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cloudexmachina.io/website-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cloudexmachina.io/legal/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://trust.cloudexmachina.io/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloudexmachina/
- group: other
  title: ''
  type: Product
  url: https://www.cloudexmachina.io/product
- group: build
  title: ''
  type: Packages
  url: packages/cloudexmachina-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudexmachina-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cloudexmachina-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cloudexmachina-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cloudexmachina-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cloudexmachina-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cloudexmachina-llms.txt
coverage:
  checked: '2026-08-17'
  detail: Cloud ex Machina is a real software company that ships a per-tenant SaaS product (Dex) and genuinely maintains public Docusaurus documentation, but it operates no developer program at all — no API reference among the 23 pages in its docs sitemap, no api.cloudexmachina.io host in DNS, no MCP server, no agent card, and no client SDK in any language registry; its only developer-facing distributables are AWS onboarding IaC (a Terraform Registry module at v0.6.0, a CloudFormation template, and a GitHub Action).
  evidence:
  - status: 200
    url: https://docs.cloudexmachina.io/sitemap.xml
  - status: 0
    url: https://api.cloudexmachina.io/openapi.json
  - status: 200
    url: https://app.cloudexmachina.io/openapi.json
  - status: 404
    url: https://www.cloudexmachina.io/.well-known/agent-card.json
  - status: 200
    url: https://registry.terraform.io/v1/modules/cxmlabs/cxm-integration/aws
  reason: no-developer-program
  state: none
created: '2026-08-17'
description: Cloud ex Machina (CxM) builds Dex, an agentic AI teammate for cloud cost and governance management. Dex continuously maps AWS, Azure, GCP and Kubernetes estates read-only and agentless, infers resource ownership by keeping the cloud connected to the organization's people and code, investigates cost and governance findings, and delivers review-ready remediation — pull requests, scripts and CLI instructions — to the engineers who can act, inside the tools they already use. The platform integrates with GitHub, GitLab, Jira, Linear, Notion, ServiceNow, Slack and Microsoft Teams, ingests non-cloud AI spend from Anthropic, and runs as a per-tenant SaaS with SAML 2.0 SSO. Cloud ex Machina publishes no public REST API or machine-readable specification; its developer-facing surface is cloud onboarding distributed as a Terraform Registry module, a CloudFormation template and a GitHub Action.
image: https://www.cloudexmachina.io/hubfs/cxm_logo.svg
layout: provider
modified: '2026-08-17'
name: Cloud Ex Machina
nav: Providers
network: true
overview: 'Cloud Ex Machina is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Infrastructure, Cloud, FinOps, and Cloud Cost Optimization.


  Cloud Ex Machina''s developer surface includes documentation, getting-started guide, engineering blog, authentication, and 17 more developer resources.'
plans:
- name: Cloudexmachina Plans Pricing
  plan_count: 0
  slug: cloudexmachina-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Cloudexmachina Rate Limits
  slug: cloudexmachina-rate-limits
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 10
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 17.5
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Cloudexmachina Authentication
  slug: cloudexmachina-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Cloudexmachina Domain Security
  slug: cloudexmachina-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cloudexmachina Trust Center
  slug: cloudexmachina-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: cloudexmachina
tags:
- Company
- Infrastructure
- Cloud
- FinOps
- Cloud Cost Optimization
- Cloud Governance
- AI Agents
- Cloud Management
- Terraform
- Kubernetes
website: https://www.cloudexmachina.io/
---
