---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 772
  human_in_the_loop: 19
  name: Akamai Technologies Agentic Access
  operation_count: 1661
  slug: akamai-technologies-agentic-access
  summary_line: 1661 operations · 772 acting · 19 human-in-the-loop
api_count: 58
apis:
- description: View which rules Adaptive Acceleration applies to a property, and generate new rules.
  name: Akamai Adaptive Acceleration API
  slug: adaptive-acceleration-v1
- description: Get notified automatically of changes in your origin infrastructure and content-delivery patterns.
  name: Akamai Alerts API
  slug: alerts-v2
- description: Provide secondary authentication to cloud, on-premises, web-based, SaaS, and IaaS applications.
  name: Akamai MFA API
  slug: amfa-v1
- description: Register and manage your APIs to enable security, delivery, and governance.
  name: Akamai API Endpoint Definition API
  slug: api-definitions-v2
- description: Create and manage API keys. Control your API traffic with quotas and throttling.
  name: Akamai API Keys and Traffic Management API
  slug: apikey-manager-api-v1
- description: Manage your configurations for Kona Site Defender, Web Application Protector, and Client Reputation.
  name: Akamai Application Security API
  slug: appsec-v1
- description: Securely store and manage access keys for cloud origins independent of your properties.
  name: Akamai Cloud Access Manager API
  slug: cam-v1
- description: Manage support requests to resolve issues with your Akamai applications and services.
  name: Akamai Case Management API
  slug: case-management-v3
- description: Refresh or remove specific cached objects, by URLs, content provider (CP) codes, or cache tags.
  name: Akamai Fast Purge API
  slug: ccu-v3
- description: Manage the lifecycle and monitor the status of your property hostnames on Akamai's China CDN.
  name: Akamai China CDN Manager API
  slug: chinacdn-v1
- description: Restrict access between your origin infrastructure and Akamai edge servers based on CIDR blocks.
  name: Akamai Client Access Control API
  slug: client-access-control-v1
- description: Seamlessly connect your publicly stored media delivery content to the Akamai edge.
  name: Akamai Cloud Wrapper Configuration API
  slug: cloud-wrapper-v1
- description: Solve specific business challenges using value-added apps that complement Akamai's core solutions.
  name: Akamai Cloudlets API
  slug: cloudlets-v2
- description: Solve specific business challenges using value-added apps that complement Akamai's core solutions.
  name: Akamai Cloudlets API
  slug: cloudlets-v3
- description: Replace or augment your DNS infrastructure with a cloud-based authoritative DNS solution.
  name: Akamai Edge DNS API
  slug: config-dns-v2
- description: Use load balancing to manage website and mobile performance demands.
  name: Akamai Global Traffic Management API
  slug: config-gtm-v1
- description: Broadcast live streaming events reliably at scale.
  name: Akamai Media Services Live Stream Provisioning API
  slug: config-media-live-v2
- description: Access detailed information about CP codes, edit their parameters, and group them for billing.
  name: Akamai CP Codes and Reporting Groups API
  slug: cprg-v1
- description: Get full life cycle management of SSL certificates for your Akamai CDN applications.
  name: Akamai Certificate Provisioning System API
  slug: cps-v2
- description: Manage and control remote access to your applications.
  name: Akamai Enterprise Application Access API
  slug: crux-v1
- description: Monitors activity on the Akamai platform and sends live log data to a destination of your choice.
  name: Akamai DataStream 2 API
  slug: datastream-config-api-v2
- description: Refresh content cached on the edge network based on directory, file extension, or other logic.
  name: Akamai Enhanced Content Control Utility API
  slug: eccu-api-v1
- description: Diagnose your server, DNS, and network problems from Akamai servers around the world.
  name: Akamai Edge Diagnostics API
  slug: edge-diagnostics-v1
- description: Add a key-value store database to your serverless compute logic and build data-driven applications.
  name: Akamai EdgeKV API
  slug: edgekv-v1
- description: Execute JavaScript functions at the edge to optimize site performance and customize web experiences.
  name: Akamai EdgeWorkers API
  slug: edgeworkers-v1
- description: A programmatic interface to manage policy settings to protect against enterprise security and acceptable user policy related events.
  name: Akamai Secure Internet Access Enterprise Configuration API
  slug: etp-config-v3
- description: Access and analyze reports for acceptable user policy (AUP) events, DNS activity, network traffic connections, security connector events, and threat events.
  name: Akamai Secure Internet Access Enterprise Reporting API
  slug: etp-report-v3
- description: Monitor and analyze Control Center events.
  name: Akamai Event Viewer API
  slug: event-viewer-v1
- description: Configure events, reporting, and alerts in Event Center.
  name: Akamai Event Center API
  slug: events-v3
- description: Get notifications of CIDR block changes on the edge network so you can update your firewall rules.
  name: Akamai Firewall Rules Notification API
  slug: firewall-rules-manager-v1
- description: Get read-only reports on Global Traffic Management's real-time statistics.
  name: Akamai Global Traffic Management Reporting API
  slug: gtm-api-v1
- description: Submit load data for a Global Traffic Management domain in either JSON or XML.
  name: Akamai Global Traffic Management Load Feedback API
  slug: gtm-load-data-v1
- description: Create users and groups, and define policies that manage access to Control Center applications.
  name: Akamai Identity and Access Management API
  slug: identity-management-v1
- description: Create users and groups, and define policies that manage access to Control Center applications.
  name: Akamai Identity and Access Management API
  slug: identity-management-v2
- description: Create users and groups, and define policies that manage access to Control Center applications.
  name: Akamai Identity and Access Management API
  slug: identity-management-v3
- description: Automate image and video delivery optimizations for your website visitors.
  name: Akamai Image & Video Manager API
  slug: imaging-v2
- description: Shield your site from DDoS attacks by diverting traffic and scrubbing network packets.
  name: Akamai Prolexic IP Protect Configuration API
  slug: ip-protect-v1
- description: Manage the public keys that authenticate JSON web token requests for IoT devices.
  name: Akamai IoT Token Access Control API
  slug: jwt-api-v1
- description: Archive live streams in HLS and DASH formats for use as video on demand (VOD) content.
  name: Akamai Live Archive Management API
  slug: live-archive-v1
- description: Monitor traffic for Media Services Live solutions.
  name: Akamai Media Services Live Reports API
  slug: media-reports-v1
- description: Akamai NetStorage Usage API — 7 operations published by Akamai Technologies in the akamai/akamai-apis OpenAPI repository.
  name: Akamai NetStorage Usage API
  slug: netstorage-usage-api
- description: Define and manage inbound access control lists (ACLs) enforced at the edge of the Prolexic cloud-based DDoS protection platform.
  name: Akamai Prolexic Network Cloud Firewall API
  slug: network-cloud-firewall-v1
- description: Automate the creation, deployment, and management of lists used in Akamai security products
  name: Akamai Network Lists API
  slug: network-lists-v2
- description: Securely update vehicle-specific software over cellular networks.
  name: Akamai IoT OTA Updates API
  slug: ota-v1
- description: Define rules and behaviors that govern your website delivery based on match criteria.
  name: Akamai Property Manager API
  slug: papi-v1
- description: Stop DDoS attacks in the cloud before they reach the data center.
  name: Akamai Prolexic Analytics API
  slug: prolexic-analytics-v2
- description: Provides network traffic visibility through Akamai's network to diagnose network issues without relying solely on third-party tools.
  name: Akamai Prolexic Network Health API
  slug: prolexic-network-health-v1
- description: Generate custom reports to monitor and optimize your Akamai services.
  name: Akamai Reporting API
  slug: reporting-api-v1
- description: Generate custom reports to monitor and optimize your Akamai services.
  name: Akamai Reporting API
  slug: reporting-api-v2
- description: Create an isolated development environment to test code changes locally before deploying to the CDN.
  name: Akamai Sandbox API
  slug: sandbox-api-v1
- description: Minimize JavaScript performance impact by retrieving or creating Script Management policies.
  name: Akamai Script Management API
  slug: script-management
- description: Integrate third-party SIEM applications with Akamai security solutions.
  name: Akamai SIEM Integration API
  slug: siem-v1
- description: Hide websites and applications from the Internet and restrict clients from accessing the origin.
  name: Akamai Site Shield API
  slug: siteshield-v1
- description: Access the SLA test configurations and the resulting reports.
  name: Akamai Service-Level Agreement API
  slug: sla-api-v1
- description: Store content for digital optimization and flexible data transfer.
  name: Akamai NetStorage Configuration API
  slug: storage-v1
- description: Recognize and flag authentication tokens that have been hijacked, and block requests that include them.
  name: Akamai Access Revocation API
  slug: taas-v2
- description: Run functional tests to check how configuration changes affect your configuration.
  name: Akamai Test Center API
  slug: test-management-v3
- description: Akamai Cloud Computing (Linode) API — provision and manage compute instances, Kubernetes (LKE), block and object storage, networking, databases, DNS and account resources.
  name: Akamai Linode API
  slug: linode-api
artifact_total: 73
asyncapis:
- description: ''
  name: Akamai Technologies Event Surface
  slug: akamai-technologies-event-surface
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Akamai Fast Purge (CCU v3) Deletions API
  slug: open-akamai-technologies-deletions-api
- collection_type: open
  name: Akamai Fast Purge (CCU v3) Deletions Invalidations API
  slug: open-akamai-technologies-invalidations-api
- collection_type: open
  name: Akamai Fast Purge (CCU v3) Deletions Status API
  slug: open-akamai-technologies-status-api
- collection_type: open
  name: Akamai Fast Purge (CCU v3) API
  slug: open-akamai-technologies
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/akamai-technologies-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/akamai-technologies-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/akamai-technologies-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/akamai-technologies-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.akamai.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://techdocs.akamai.com
- group: docs
  title: ''
  type: Documentation
  url: https://techdocs.akamai.com/home
- group: docs
  title: ''
  type: APIReference
  url: https://techdocs.akamai.com/home/page/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://techdocs.akamai.com/developer/docs/make-your-first-api-call
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/akamai
- group: company
  title: ''
  type: Blog
  url: https://developers.akamai.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://login.linode.com/signup
- group: start
  title: ''
  type: Login
  url: https://control.akamai.com
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/akamai/akamai-apis
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/akamai-technologies
- group: operate
  title: ''
  type: StatusPage
  url: https://www.akamaistatus.com
- group: build
  title: ''
  type: Packages
  url: packages/akamai-technologies-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/akamai-technologies-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/akamai-technologies-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/akamai-technologies-api-catalog.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/akamai-technologies-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/akamai-technologies-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/akamai-technologies-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/akamai-technologies-ccu-v3-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/akamai-technologies-papi-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/akamai-technologies-edgeworkers-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/akamai-technologies-config-dns-v2-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/akamai-technologies-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/akamai-technologies-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/akamai-technologies-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/akamai-technologies-lifecycle.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/akamai-technologies-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/akamai-technologies-vulnerability-disclosure.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/akamai-technologies-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/akamai-technologies-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/akamai-technologies-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/akamai-technologies-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/akamai-technologies-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/akamai-technologies-event-surface.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/akamai-technologies-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/akamai-technologies-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/akamai-technologies-finops.yml
created: '2026-04-19'
description: Akamai Technologies operates one of the world's largest distributed edge platforms, spanning content delivery (Ion, Adaptive Media Delivery, Download Delivery), application and API security (App & API Protector, Bot Manager, Prolexic DDoS, Secure Internet Access, Guardicore segmentation), edge compute (EdgeWorkers, EdgeKV, Akamai Functions), DNS and traffic management (Edge DNS, Global Traffic Management), NetStorage, and Akamai Cloud Computing - the Linode-based public cloud acquired in 2022. Akamai publishes first-party OpenAPI descriptions for its control-plane APIs in the akamai/akamai-apis GitHub repository and for the Linode API in linode/linode-api-openapi, covering property configuration, certificate provisioning, purge, identity and access management, security configuration, reporting, diagnostics, test automation and cloud provisioning. All Akamai control-plane APIs authenticate with the EdgeGrid HMAC-SHA256 request-signing scheme against a per-account hostname; the
  Linode API uses OAuth 2.0 and personal access tokens.
finops:
- name: Akamai Technologies Finops
  service_category: CDN + Edge + Cloud
  slug: akamai-technologies-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/akamai-technologies.png
layout: provider
mcp_servers:
- description: Akamai publishes one official Model Context Protocol server, akamai-cloud-mcp, covering Akamai Cloud (Linode). It is read-only by construction - a GET-only HTTP client, an allowlist serializer and a r
  name: Akamai Cloud MCP Server
  slug: akamai-cloud-mcp-server
modified: '2026-08-30'
name: Akamai Technologies
nav: Providers
network: true
overview: 'Akamai Technologies publishes 58 APIs on the [APIs.io](https://apis.io/) network, including Akamai Adaptive Acceleration API, Akamai Alerts API, Akamai MFA API, and 55 more. Tagged areas include CDN, Security, Cloud, Edge Computing, and DNS.


  The Akamai Technologies catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Akamai Technologies'' developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, signup flow, sandbox, and 36 more developer resources.'
plans:
- name: Akamai Technologies Plans Pricing
  plan_count: 13
  slug: akamai-technologies-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 8
  name: Akamai Technologies Rate Limits
  slug: akamai-technologies-rate-limits
scopes:
- name: Akamai Technologies Scopes
  scope_count: 37
  slug: akamai-technologies-scopes
  summary_line: 37 scopes · authorizationCode
score:
  band: developing
  composite: 50.1
  coverage:
    artifact_dirs: 26
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 5.8
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 53.8
    developer_ergonomics: 36.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 92.1
  previous_composite: 44.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 4.7
      derived: 0
      marker_coverage: 0.0
      total: 43
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/akamai-technologies/refs/heads/main/screenshots/akamai-technologies-2026-06-20T171446.png
security:
- kind: authentication
  name: Akamai Technologies Authentication
  slug: akamai-technologies-authentication
  summary_line: http/oauth2/custom-signature · 3 schemes
- kind: domain-security
  name: Akamai Technologies Domain Security
  slug: akamai-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Akamai Technologies Vulnerability Disclosure
  slug: akamai-technologies-vulnerability-disclosure
  summary_line: Hackerone
slug: akamai-technologies
tags:
- CDN
- Security
- Cloud
- Edge Computing
- DNS
- Content Delivery
- Cloud Computing
- Zero Trust
- Media Delivery
- Observability
- Infrastructure
- Kubernetes
website: https://www.akamai.com
---
