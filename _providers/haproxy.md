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
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.5
  scored_at: '2026-09-16'
api_count: 1
apis:
- description: 'The HAProxy Runtime API (formerly known as the stats socket) is a socket-based interface for dynamically managing HAProxy at runtime. It allows operators to enable or disable servers, adjust weights, '
  name: HAProxy Runtime API
  slug: haproxy-runtime-api
- description: The HAProxy Kubernetes Ingress Controller implements routing rules defined in Kubernetes Ingress resources, dynamically updating HAProxy configuration as pods are added or removed from the cluster. It
  name: HAProxy Kubernetes Ingress Controller
  slug: haproxy-kubernetes-ingress-controller
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The ACL API from HAProxy — 8 operation(s) for acl.
  name: HAProxy ACL API
  slug: haproxy-acl-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The ACL Runtime API from HAProxy — 4 operation(s) for acl runtime.
  name: HAProxy ACL Runtime API
  slug: haproxy-acl-runtime-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The Acme API from HAProxy — 2 operation(s) for acme.
  name: HAProxy Acme API
  slug: haproxy-acme-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The AcmeRuntime API from HAProxy — 1 operation(s) for acmeruntime.
  name: HAProxy Acme Runtime API
  slug: haproxy-acmeruntime-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: Managing backend configurations (advanced mode)
  name: HAProxy Backend API
  slug: haproxy-backend-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The BackendSwitchingRule API from HAProxy — 2 operation(s) for backendswitchingrule.
  name: HAProxy Backend Switching Rule API
  slug: haproxy-backendswitchingrule-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: Managing frontend bind configurations (advanced mode)
  name: HAProxy Bind API
  slug: haproxy-bind-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The Cache API from HAProxy — 2 operation(s) for cache.
  name: HAProxy Cache API
  slug: haproxy-cache-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: Raw HAProxy configuration management (advanced mode)
  name: HAProxy Configuration API
  slug: haproxy-configuration-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The CrtLoad API from HAProxy — 2 operation(s) for crtload.
  name: HAProxy Crt Load API
  slug: haproxy-crtload-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The CrtStore API from HAProxy — 2 operation(s) for crtstore.
  name: HAProxy Crt Store API
  slug: haproxy-crtstore-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The DeclareCapture API from HAProxy — 2 operation(s) for declarecapture.
  name: HAProxy Declare Capture API
  slug: haproxy-declarecapture-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: Managing defaults configuration (advanced mode)
  name: HAProxy Defaults API
  slug: haproxy-defaults-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The DgramBind API from HAProxy — 2 operation(s) for dgrambind.
  name: HAProxy Dgram Bind API
  slug: haproxy-dgrambind-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: API autodiscover endpoints
  name: HAProxy Discovery API
  slug: haproxy-discovery-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The FCGIApp API from HAProxy — 2 operation(s) for fcgiapp.
  name: HAProxy FCGI App API
  slug: haproxy-fcgiapp-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The Filter API from HAProxy — 4 operation(s) for filter.
  name: HAProxy Filter API
  slug: haproxy-filter-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The ForceBeSwitch API from HAProxy — 2 operation(s) for forcebeswitch.
  name: HAProxy Force Be Switch API
  slug: haproxy-forcebeswitch-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: Managing frontend configuration (advanced mode)
  name: HAProxy Frontend API
  slug: haproxy-frontend-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: Managing global configuration (advanced mode)
  name: HAProxy Global API
  slug: haproxy-global-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The Group API from HAProxy — 2 operation(s) for group.
  name: HAProxy Group API
  slug: haproxy-group-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The Health API from HAProxy — 1 operation(s) for health.
  name: HAProxy Health API
  slug: haproxy-health-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The HTTPAfterResponseRule API from HAProxy — 6 operation(s) for httpafterresponserule.
  name: HAProxy HTTP After Response Rule API
  slug: haproxy-httpafterresponserule-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The HTTPCheck API from HAProxy — 6 operation(s) for httpcheck.
  name: HAProxy HTTP Check API
  slug: haproxy-httpcheck-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The HTTPErrorRule API from HAProxy — 6 operation(s) for httperrorrule.
  name: HAProxy HTTP Error Rule API
  slug: haproxy-httperrorrule-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The HTTPErrors API from HAProxy — 2 operation(s) for httperrors.
  name: HAProxy HTTP Errors API
  slug: haproxy-httperrors-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The HTTPRequestRule API from HAProxy — 6 operation(s) for httprequestrule.
  name: HAProxy HTTP Request Rule API
  slug: haproxy-httprequestrule-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The HTTPResponseRule API from HAProxy — 6 operation(s) for httpresponserule.
  name: HAProxy HTTP Response Rule API
  slug: haproxy-httpresponserule-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The Information API from HAProxy — 2 operation(s) for information.
  name: HAProxy Information API
  slug: haproxy-information-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The LogForward API from HAProxy — 2 operation(s) for logforward.
  name: HAProxy Log Forward API
  slug: haproxy-logforward-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The LogProfile API from HAProxy — 2 operation(s) for logprofile.
  name: HAProxy Log Profile API
  slug: haproxy-logprofile-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The LogTarget API from HAProxy — 12 operation(s) for logtarget.
  name: HAProxy Log Target API
  slug: haproxy-logtarget-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The MailerEntry API from HAProxy — 2 operation(s) for mailerentry.
  name: HAProxy Mailer Entry API
  slug: haproxy-mailerentry-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The Mailers API from HAProxy — 2 operation(s) for mailers.
  name: HAProxy Mailers API
  slug: haproxy-mailers-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The Maps API from HAProxy — 4 operation(s) for maps.
  name: HAProxy Maps API
  slug: haproxy-maps-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The Nameserver API from HAProxy — 2 operation(s) for nameserver.
  name: HAProxy Nameserver API
  slug: haproxy-nameserver-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The Peer API from HAProxy — 2 operation(s) for peer.
  name: HAProxy Peer API
  slug: haproxy-peer-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The PeerEntry API from HAProxy — 2 operation(s) for peerentry.
  name: HAProxy Peer Entry API
  slug: haproxy-peerentry-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The QUICInitialRule API from HAProxy — 4 operation(s) for quicinitialrule.
  name: HAProxy QUIC Initial Rule API
  slug: haproxy-quicinitialrule-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: Checking reload success. To avoid constant reloading we reload in intervals that are configurable when with reload-delay option. When a change to configuration is made and force_reload url query strin
  name: HAProxy Reloads API
  slug: haproxy-reloads-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The Resolver API from HAProxy — 2 operation(s) for resolver.
  name: HAProxy Resolver API
  slug: haproxy-resolver-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The Ring API from HAProxy — 2 operation(s) for ring.
  name: HAProxy Ring API
  slug: haproxy-ring-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: Managing backend server configurations (advanced mode)
  name: HAProxy Server API
  slug: haproxy-server-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The ServerSwitchingRule API from HAProxy — 2 operation(s) for serverswitchingrule.
  name: HAProxy Server Switching Rule API
  slug: haproxy-serverswitchingrule-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The ServerTemplate API from HAProxy — 2 operation(s) for servertemplate.
  name: HAProxy Server Template API
  slug: haproxy-servertemplate-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: Managing sites (simple configuration mode). Sites are considered as one frontend with multiple backends connected to it via default_backend or use-backend directives.
  name: HAProxy Sites API
  slug: haproxy-sites-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The Specification API from HAProxy — 1 operation(s) for specification.
  name: HAProxy Specification API
  slug: haproxy-specification-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The SpecificationOpenapiv3 API from HAProxy — 1 operation(s) for specificationopenapiv3.
  name: HAProxy Specification Openapiv3 API
  slug: haproxy-specificationopenapiv3-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The Spoe API from HAProxy — 11 operation(s) for spoe.
  name: HAProxy Spoe API
  slug: haproxy-spoe-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The SpoeTransactions API from HAProxy — 2 operation(s) for spoetransactions.
  name: HAProxy Spoe Transactions API
  slug: haproxy-spoetransactions-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The SSLFrontUse API from HAProxy — 2 operation(s) for sslfrontuse.
  name: HAProxy SSL Front Use API
  slug: haproxy-sslfrontuse-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The SSLRuntime API from HAProxy — 10 operation(s) for sslruntime.
  name: HAProxy SSL Runtime API
  slug: haproxy-sslruntime-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: Stats container
  name: HAProxy Stats API
  slug: haproxy-stats-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The StickRule API from HAProxy — 2 operation(s) for stickrule.
  name: HAProxy Stick Rule API
  slug: haproxy-stickrule-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The StickTable API from HAProxy — 3 operation(s) for sticktable.
  name: HAProxy Stick Table API
  slug: haproxy-sticktable-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The Storage API from HAProxy — 9 operation(s) for storage.
  name: HAProxy Storage API
  slug: haproxy-storage-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The Table API from HAProxy — 2 operation(s) for table.
  name: HAProxy Table API
  slug: haproxy-table-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The TCPCheck API from HAProxy — 6 operation(s) for tcpcheck.
  name: HAProxy TCP Check API
  slug: haproxy-tcpcheck-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The TCPRequestRule API from HAProxy — 6 operation(s) for tcprequestrule.
  name: HAProxy TCP Request Rule API
  slug: haproxy-tcprequestrule-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The TCPResponseRule API from HAProxy — 4 operation(s) for tcpresponserule.
  name: HAProxy TCP Response Rule API
  slug: haproxy-tcpresponserule-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The Traces API from HAProxy — 2 operation(s) for traces.
  name: HAProxy Traces API
  slug: haproxy-traces-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: Managing transactions. Configuration changes can be grouped in the transaction. You start the transaction with trasactions POST, and call the configuration changes you need with parameter transaction_
  name: HAProxy Transactions API
  slug: haproxy-transactions-api
- baseURL: http://{haproxy-host}:5555/v3
  baseurl_source: declared
  description: The User API from HAProxy — 2 operation(s) for user.
  name: HAProxy User API
  slug: haproxy-user-api
- baseURL: http://{haproxy-host}:5555/v3/services/haproxy/runtime
  baseurl_source: declared
  description: The Health Check API from HAProxy — 2 operation(s) for health check.
  name: HAProxy Health Check API
  slug: haproxy-health-check-api
- baseURL: http://{haproxy-host}:5555/v3/services/haproxy/runtime
  baseurl_source: declared
  description: The Service Discovery API from HAProxy — 4 operation(s) for service discovery.
  name: HAProxy Service Discovery API
  slug: haproxy-service-discovery-api
- baseURL: http://{haproxy-host}:5555/v3/services/haproxy/runtime
  baseurl_source: declared
  description: The User List API from HAProxy — 2 operation(s) for user list.
  name: HAProxy User List API
  slug: haproxy-user-list-api
artifact_total: 73
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/haproxy/refs/heads/main/overlays/haproxy-data-plane-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/haproxy-data-plane-api-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/haproxy/refs/heads/main/authentication/haproxy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/haproxy-authentication.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/haproxytech/dataplaneapi/issues
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/haproxytech/dataplaneapi/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/haproxytech/dataplaneapi/blob/master/LICENSE
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/haproxy/refs/heads/main/security/haproxy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/haproxy-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/haproxy-technologies
- group: company
  title: ''
  type: Website
  url: https://www.haproxy.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.haproxy.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/haproxy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/haproxytech
- group: operate
  title: ''
  type: Community
  url: https://discourse.haproxy.org/
- group: company
  title: ''
  type: Blog
  url: https://www.haproxy.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.haproxy.com/support/support-options
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.haproxy.com/legal
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/haproxy/refs/heads/main/conventions/haproxy-conventions.yml
  title: ''
  type: Conventions
  url: conventions/haproxy-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/haproxy/refs/heads/main/conventions/haproxy-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/haproxy-conventions.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/haproxy/refs/heads/main/packages/haproxy-packages.yml
  title: ''
  type: Packages
  url: packages/haproxy-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/haproxy/refs/heads/main/packages/haproxy-packages.yml
  title: ''
  type: SDKs
  url: packages/haproxy-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/haproxy/refs/heads/main/cli/haproxy-cli.yml
  title: ''
  type: CLI
  url: cli/haproxy-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/haproxy/refs/heads/main/lifecycle/haproxy-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/haproxy-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/haproxy/refs/heads/main/lifecycle/haproxy-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/haproxy-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/haproxy/refs/heads/main/changelog/haproxy-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/haproxy-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/haproxy/refs/heads/main/conformance/haproxy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/haproxy-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/haproxy/refs/heads/main/errors/haproxy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/haproxy-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/haproxy/refs/heads/main/data-model/haproxy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/haproxy-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/haproxy/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/haproxy/refs/heads/main/llms/haproxy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/haproxy-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/haproxy/refs/heads/main/plans/haproxy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/haproxy-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/haproxy/refs/heads/main/rate-limits/haproxy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/haproxy-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/haproxy/refs/heads/main/finops/haproxy-finops.yml
  title: ''
  type: FinOps
  url: finops/haproxy-finops.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.haproxy.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://my.haproxy.com/portal/cust/login
created: '2026-03-16'
description: HAProxy is a free, very fast and reliable reverse-proxy offering high availability, load balancing, and proxying for TCP and HTTP-based applications. It exposes a Data Plane API for dynamic configuration management and a stats socket for runtime management.
finops:
- name: Haproxy Finops
  service_category: API
  slug: haproxy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/haproxy.png
layout: provider
modified: '2026-08-28'
name: HAProxy
nav: Providers
network: true
overview: 'HAProxy publishes 66 APIs on the [APIs.io](https://apis.io/) network, including ACL API, ACL Runtime API, Acme API, and 63 more. Tagged areas include High Availability, Load Balancing, Networking, Reverse Proxy, and Proxy.


  HAProxy''s developer surface includes authentication, documentation, engineering blog, support, CLI, changelog, and 27 more developer resources.'
plans:
- name: Haproxy Plans Pricing
  plan_count: 0
  slug: haproxy-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Haproxy Rate Limits
  slug: haproxy-rate-limits
score:
  band: developing
  composite: 42.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.2
  facets:
    access_clarity: 35.5
    contract_governance: 4.5
    contract_quality: 53.9
    developer_ergonomics: 63.7
    discoverability: 53.7
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 50.0
  previous_composite: 43.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 66
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/haproxy/refs/heads/main/screenshots/haproxy-2026-06-20T182509.png
security:
- kind: authentication
  name: Haproxy Authentication
  slug: haproxy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Haproxy Domain Security
  slug: haproxy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: haproxy
tags:
- High Availability
- Load Balancing
- Networking
- Reverse Proxy
- Proxy
- Kubernetes
- Ingress
- Open-Source
- Infrastructure
- Application Delivery
website: https://www.haproxy.org/
---
