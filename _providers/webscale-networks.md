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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://api.webscale.com/v2
  baseurl_source: declared
  description: The Webscale v2 control-plane REST API. 151 operations across 25 resource collections — applications and web controls, address sets, URL maps, clusters, environments and stacks, servers, builders, mon
  name: Webscale APIs
  slug: webscale-apis
artifact_total: 8
asyncapis:
- description: ''
  name: Webscale Networks Webhooks
  slug: webscale-networks-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/webscale-networks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.webscale.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://control.webscale.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.webscale.com/
- group: docs
  title: ''
  type: APIReference
  url: https://control.webscale.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.webscale.com/docs/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://www.webscale.com/support-managed-services/
- group: company
  title: ''
  type: Blog
  url: https://www.webscale.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/webscale-networks
- group: commercial
  title: ''
  type: Pricing
  url: https://www.webscale.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://control.webscale.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.webscale.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.webscale.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.magemojo.com/
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://www.webscale.com/sla/
- group: auth
  title: ''
  type: TrustCenter
  url: security/webscale-networks-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/webscale-networks-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/webscale-networks-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/webscale-networks-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/webscale-networks-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/webscale-networks-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/webscale-networks-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/webscale-networks-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/webscale-networks-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/webscale-networks-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/webscale-networks-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/webscale-networks-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/webscale-networks-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.webscale.com/llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/webscale-networks-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/webscale-networks-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/webscale-networks-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/webscale-networks-problem-types.yml
created: '2026-09-04'
description: Webscale Networks is a commerce infrastructure and application delivery company that runs managed AWS cloud hosting, CDN, WAF and edge traffic control for Adobe Commerce, Magento, Shopware, WooCommerce and headless storefronts, layered with an agentic AI product line (Agentic Commerce OS) covering a customer data platform, AI segmentation and an AI shopping assistant. It absorbed edge-computing company Section.io in 2023 and the MageMojo/Stratus hosting business, and exposes the whole platform through the Webscale APIs — a RESTful v2 control-plane API covering applications, web controls, clusters, environments, servers, monitors, logs, metrics, files, secrets, tasks, SSH hosts, accounts, users, roles and access keys — documented with a public OpenAPI 3.0.3 description served from its own control console.
image: https://www.webscale.com/wp-content/uploads/2025/05/ws-logo.svg
layout: provider
modified: '2026-09-04'
name: Webscale Networks
nav: Providers
network: true
overview: 'Webscale Networks publishes 1 API on the [APIs.io](https://apis.io/) network: Webscale APIs. Tagged areas include Ecommerce, Cloud Hosting, Content Delivery Network, Application Delivery, and Web Application Firewall.


  The Webscale Networks catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Webscale Networks'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 27 more developer resources.'
plans:
- name: Webscale Networks Plans Pricing
  plan_count: 3
  slug: webscale-networks-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Webscale Networks Rate Limits
  slug: webscale-networks-rate-limits
score:
  band: strong
  composite: 62.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.8
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 60.4
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 62.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Webscale Networks Authentication
  slug: webscale-networks-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Webscale Networks Domain Security
  slug: webscale-networks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Webscale Networks Vulnerability Disclosure
  slug: webscale-networks-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Webscale Networks Trust Center
  slug: webscale-networks-trust-center
  summary_line: SOC 2 Type 2
slug: webscale-networks
tags:
- Ecommerce
- Cloud Hosting
- Content Delivery Network
- Application Delivery
- Web Application Firewall
- Edge Computing
- Managed Hosting
- Infrastructure
- Magento
- Adobe Commerce
- Observability
website: https://www.webscale.com/
---
