---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 72.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://domscan.net
  baseurl_source: spec
  description: The Agent Readiness API from DomScan — 1 operation(s) for agent readiness.
  name: DomScan Agent Readiness API
  slug: domscan-agent-readiness-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: The Batch API from DomScan — 4 operation(s) for batch.
  name: DomScan Batch API
  slug: domscan-batch-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: The Brand Protection API from DomScan — 5 operation(s) for brand protection.
  name: DomScan Brand Protection API
  slug: domscan-brand-protection-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: Brand name quality scoring and comparison
  name: DomScan Brand Scoring API
  slug: domscan-brand-scoring-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: Reference datasets and coverage metadata
  name: DomScan Dataset API
  slug: domscan-dataset-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: DNS record lookup, security analysis, and propagation checking
  name: DomScan DNS API
  slug: domscan-dns-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: Review lookup-driven, day-level DNS observations from DomScan
  name: DomScan DNS History API
  slug: domscan-dns-history-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: Check if domains are available for registration using RDAP
  name: DomScan Domain Availability API
  slug: domscan-domain-availability-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: Comprehensive domain health analysis including DNS, SSL, and security
  name: DomScan Domain Health API
  slug: domscan-domain-health-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: Domain comparison, scoring, popularity, lifecycle, and profile intelligence
  name: DomScan Domain Intelligence API
  slug: domscan-domain-intelligence-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: Registration lifecycle, expiry, renewal, and deletion timing signals
  name: DomScan Domain Lifecycle API
  slug: domscan-domain-lifecycle-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: AI-powered domain name suggestions with availability checking
  name: DomScan Domain Suggestions API
  slug: domscan-domain-suggestions-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: Algorithmic domain value estimation based on multiple factors
  name: DomScan Domain Valuation API
  slug: domscan-domain-valuation-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: Email blacklist checking, disposable domain detection, and email validation
  name: DomScan Email API
  slug: domscan-email-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: Build and validate SPF, DMARC, and DKIM records
  name: DomScan Email Authentication API
  slug: domscan-email-authentication-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: Detect hosting providers, CDN, WAF, and email providers
  name: DomScan Hosting Detection API
  slug: domscan-hosting-detection-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: Network and hosting infrastructure discovery
  name: DomScan Infrastructure API
  slug: domscan-infrastructure-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: IP geolocation, ASN lookup, and reverse DNS
  name: DomScan IP Intelligence API
  slug: domscan-ip-intelligence-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: API information and system endpoints
  name: DomScan Meta API
  slug: domscan-meta-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: Open source intelligence tools for domain analysis
  name: DomScan OSINT API
  slug: domscan-osint-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: Privacy-first phone number validation and formatting against bundled numbering-plan metadata
  name: DomScan Phone Intelligence API
  slug: domscan-phone-intelligence-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: Scheduled standard-TLD rows from official sources and separate exact-domain quotes. Current public provider coverage and source scope are documented per integration.
  name: DomScan Pricing API
  slug: domscan-pricing-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: Typed RDAP lookups and related registration analysis
  name: DomScan RDAP API
  slug: domscan-rdap-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: Compound API endpoints bundling multiple services with credit savings
  name: DomScan Recipes API
  slug: domscan-recipes-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: Security posture, reputation, exposure, and vulnerability intelligence
  name: DomScan Security API
  slug: domscan-security-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: Social media handle availability checking
  name: DomScan Social API
  slug: domscan-social-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: SSL certificate grading, chain analysis, and expiry monitoring
  name: DomScan SSL Analysis API
  slug: domscan-ssl-analysis-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: TLS certificate, protocol, and transport security checks
  name: DomScan SSL API
  slug: domscan-ssl-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: Certificate transparency search and subdomain discovery
  name: DomScan SSL Certificates API
  slug: domscan-ssl-certificates-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: TLD information, comparison, and coverage data
  name: DomScan TLD Intelligence API
  slug: domscan-tld-intelligence-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: Detect typosquatting and brand impersonation risks
  name: DomScan Typosquatting API
  slug: domscan-typosquatting-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: API key management and usage statistics (requires login)
  name: DomScan User API
  slug: domscan-user-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: Domain monitoring for expiration and availability (requires login)
  name: DomScan Watchlist API
  slug: domscan-watchlist-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: Tech stack detection, categorization, and reputation
  name: DomScan Web Intelligence API
  slug: domscan-web-intelligence-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: Domain registration data lookup via RDAP and WHOIS
  name: DomScan WHOIS/RDAP API
  slug: domscan-whois-rdap-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: Bank details, VAT numbers, healthcare providers and sanctions screening against official registers and lists
  name: DomScan Business Verification API
  slug: domscan-business-verification-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: US healthcare provider lookup and verification by NPI
  name: DomScan Healthcare API
  slug: domscan-healthcare-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: Website legal pages, consent tooling and trackers
  name: DomScan Privacy API
  slug: domscan-privacy-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: The SEO API from DomScan — 16 operation(s) for seo.
  name: DomScan SEO API
  slug: domscan-seo-api
- baseURL: https://domscan.net
  baseurl_source: spec
  description: Signed monitoring alerts delivered to your HTTPS endpoints, billed per delivered alert
  name: DomScan Webhooks API
  slug: domscan-webhooks-api
artifact_total: 53
asyncapis:
- description: ''
  name: Domscan Webhooks
  slug: domscan-webhooks
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://domscan.net/blog/rss.xml
- group: other
  href: https://artifacts.apis.io/domscan/capabilities/domscan-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/domscan-capability-edges.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://domscan.net/mcp
- group: company
  title: ''
  type: Website
  url: https://domscan.net
- group: auth
  href: https://artifacts.apis.io/domscan/security/domscan-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/domscan-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/domscan/authentication/domscan-authentication.yml
  title: ''
  type: Authentication
  url: authentication/domscan-authentication.yml
- group: agent
  href: https://artifacts.apis.io/domscan/well-known/domscan-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/domscan-well-known.yml
- group: agent
  href: https://artifacts.apis.io/domscan/mcp/domscan-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/domscan-mcp.yml
- group: auth
  href: https://artifacts.apis.io/domscan/scopes/domscan-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/domscan-scopes.yml
- group: design
  href: https://artifacts.apis.io/domscan/errors/domscan-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/domscan-problem-types.yml
- group: design
  href: https://artifacts.apis.io/domscan/lifecycle/domscan-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/domscan-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/domscan/changelog/domscan-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/domscan-changelog.yml
- group: design
  href: https://artifacts.apis.io/domscan/conventions/domscan-conventions.yml
  title: ''
  type: Conventions
  url: conventions/domscan-conventions.yml
- group: design
  href: https://artifacts.apis.io/domscan/conventions/domscan-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/domscan-conventions.yml
- group: design
  href: https://artifacts.apis.io/domscan/conformance/domscan-conformance.yml
  title: ''
  type: Conformance
  url: conformance/domscan-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/domscan/plans/domscan-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/domscan-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/domscan/rate-limits/domscan-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/domscan-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/domscan/data-model/domscan-data-model.yml
  title: ''
  type: DataModel
  url: data-model/domscan-data-model.yml
- group: build
  href: https://artifacts.apis.io/domscan/cli/domscan-cli.yml
  title: ''
  type: CLI
  url: cli/domscan-cli.yml
- group: build
  href: https://artifacts.apis.io/domscan/packages/domscan-packages.yml
  title: ''
  type: Packages
  url: packages/domscan-packages.yml
- group: build
  href: https://artifacts.apis.io/domscan/packages/domscan-packages.yml
  title: ''
  type: SDKs
  url: packages/domscan-packages.yml
- group: design
  href: https://artifacts.apis.io/domscan/asyncapi/domscan-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/domscan-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/domscan/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/domscan/overlays/domscan-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/domscan-openapi-overlay.yaml
- group: docs
  title: ''
  type: APIReference
  url: https://domscan.net/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://domscan.net/quickstart
- group: company
  title: ''
  type: Blog
  url: https://domscan.net/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://domscan.net/pricing
- group: start
  title: ''
  type: SignUp
  url: https://domscan.net/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://domscan.net/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://domscan.net/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/estevecastells
created: '2026-07-12'
description: Domain intelligence API for domain availability, DNS, WHOIS/RDAP, valuation, security checks, email posture, social handle checks, and monitoring workflows. Offers REST API, machine-readable contracts, a hosted MCP server, and llms.txt.
finops:
- has_sources: true
  method: derived
  name: Domscan Finops
  primary_unit: credits
  service_category: ''
  slug: domscan-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/domscan.png
layout: provider
mcp_servers:
- description: ''
  name: DomScan MCP Server
  slug: mcp
modified: '2026-10-06'
name: DomScan
nav: Providers
network: true
overview: 'DomScan publishes 40 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Readiness API, Batch API, Brand Protection API, and 37 more. Tagged areas include Domains, DNS, WHOIS, RDAP, and SSL/TLS.


  The DomScan catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  DomScan''s developer surface includes authentication, changelog, CLI, API reference, getting-started guide, engineering blog, pricing, and 25 more developer resources.'
plans:
- name: Domscan Plans Pricing
  plan_count: 4
  slug: domscan-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 4
  name: Domscan Rate Limits
  slug: domscan-rate-limits
rules:
- authorship: generated
  effective_rule_count: 120
  extends:
  - spectral:oas
  name: DomScan API Rules
  rule_count: 79
  severity_counts:
    error: 53
    hint: 0
    info: 1
    warn: 25
  slug: domscan-rules
scopes:
- name: Domscan Scopes
  scope_count: 1
  slug: domscan-scopes
  summary_line: 1 scope
score:
  band: strong
  composite: 65.9
  coverage:
    artifact_dirs: 31
    catalog_earned: 63.5
    catalog_earned_first_party: 24.0
    catalog_gap: 51.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 84.2
    contract_governance: 31.8
    contract_quality: 64.4
    developer_ergonomics: 63.7
    discoverability: 66.7
    operational_transparency: 57.9
  previous_composite: 65.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 51.9
      total: 77
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/domscan/domscan-2026-07-25T212249.png
security:
- kind: authentication
  name: Domscan Authentication
  slug: domscan-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Domscan Domain Security
  slug: domscan-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: domscan-brand-protection-monitoring
  slug: domscan-brand-protection-monitoring
- name: domscan-domain-acquisition-due-diligence
  slug: domscan-domain-acquisition-due-diligence
- name: domscan-email-deliverability-audit
  slug: domscan-email-deliverability-audit
- name: domscan-find-available-domain
  slug: domscan-find-available-domain
slug: domscan
tags:
- Domains
- DNS
- WHOIS
- RDAP
- SSL/TLS
- Email Security
- Domain Valuation
- Brand Protection
- OSINT
- Threat Intelligence
- MCP
- Agent-Native
website: https://domscan.net
---
