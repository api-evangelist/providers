---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bound
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.2
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 135
  human_in_the_loop: 4
  name: Cloud Foundry Agentic Access
  operation_count: 266
  slug: cloud-foundry-agentic-access
  summary_line: 266 operations · 135 acting · 4 human-in-the-loop
api_count: 2
apis:
- description: The User Account and Authentication (UAA) server is Cloud Foundry's identity provider and OAuth 2.0 authorization server. It issues tokens consumed by the Cloud Controller, brokers, and operator tooli
  name: Cloud Foundry UAA
  slug: uaa
- description: Loggregator is Cloud Foundry's distributed log and metric pipeline that aggregates application logs, platform component logs, and metrics for streaming consumption by users and external sinks. It expo
  name: Cloud Foundry Loggregator
  slug: loggregator
- description: BOSH is Cloud Foundry's release engineering tool for packaging, deploying, and managing distributed software. The BOSH Director API exposes deployment, stemcell, release, task, and VM lifecycle operat
  name: BOSH Director API
  slug: bosh
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: The Apps API from Cloud Foundry — 4 operation(s) for apps.
  name: Cloud Foundry Apps API
  slug: cloud-foundry-apps-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: The Builds API from Cloud Foundry — 1 operation(s) for builds.
  name: Cloud Foundry Builds API
  slug: cloud-foundry-builds-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: The Deployments API from Cloud Foundry — 1 operation(s) for deployments.
  name: Cloud Foundry Deployments API
  slug: cloud-foundry-deployments-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: The Jobs API from Cloud Foundry — 1 operation(s) for jobs.
  name: Cloud Foundry Jobs API
  slug: cloud-foundry-jobs-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: The Organizations API from Cloud Foundry — 2 operation(s) for organizations.
  name: Cloud Foundry Organizations API
  slug: cloud-foundry-organizations-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: The Service Instances API from Cloud Foundry — 2 operation(s) for service instances.
  name: Cloud Foundry Service Instances API
  slug: cloud-foundry-service-instances-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: The Spaces API from Cloud Foundry — 2 operation(s) for spaces.
  name: Cloud Foundry Spaces API
  slug: cloud-foundry-spaces-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: Administrative operations for Cloud Foundry platform management.
  name: Cloud Foundry Admin API
  slug: cloud-foundry-admin-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: App usage events are a record of changes in the usage of apps and tasks.
  name: Cloud Foundry App Usage Events API
  slug: cloud-foundry-app-usage-events-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: List aggregated metrics of an application.
  name: Cloud Foundry Application Metric API V1 API
  slug: cloud-foundry-application-metric-api-v1-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: Audit events help Cloud Foundry operators monitor actions taken against resources (such as apps) via user or system actions.
  name: Cloud Foundry Audit Events API
  slug: cloud-foundry-audit-events-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: Buildpacks are used during a build to download external dependencies and transform a package into an executable droplet.
  name: Cloud Foundry Buildpacks API
  slug: cloud-foundry-buildpacks-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: The Catalog API from Cloud Foundry — 1 operation(s) for catalog.
  name: Cloud Foundry Catalog API
  slug: cloud-foundry-catalog-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: The Create Policy API V1 API from Cloud Foundry — 1 operation(s) for create policy api v1.
  name: Cloud Foundry Create Policy API V1 API
  slug: cloud-foundry-create-policy-api-v1-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: Work with application-specific custom metrics to scale your application.
  name: Cloud Foundry Custom Metrics API V1 API
  slug: cloud-foundry-custom-metrics-api-v1-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: The Delete Policy API V1 API from Cloud Foundry — 1 operation(s) for delete policy api v1.
  name: Cloud Foundry Delete Policy API V1 API
  slug: cloud-foundry-delete-policy-api-v1-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: Domains represent a fully qualified domain name that is used for application routes.
  name: Cloud Foundry Domains API
  slug: cloud-foundry-domains-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: Droplets are the result of staging an application package.
  name: Cloud Foundry Droplets API
  slug: cloud-foundry-droplets-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: 'There are two types of environment variable groups: running and staging.'
  name: Cloud Foundry Environment Variable Groups API
  slug: cloud-foundry-environment-variable-groups-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: Feature flags are runtime flags that enable or disable functionality on the API.
  name: Cloud Foundry Feature Flags API
  slug: cloud-foundry-feature-flags-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: The Get Policy API V1 API from Cloud Foundry — 1 operation(s) for get policy api v1.
  name: Cloud Foundry Get Policy API V1 API
  slug: cloud-foundry-get-policy-api-v1-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: Info endpoints expose Cloud Controller configuration information.
  name: Cloud Foundry Info API
  slug: cloud-foundry-info-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: Isolation Segments provide dedicated pools of resources to which apps can be deployed to isolate workloads.
  name: Cloud Foundry Isolation Segments API
  slug: cloud-foundry-isolation-segments-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: A manifest is a method for applying bulk configurations to apps and their underlying processes.
  name: Cloud Foundry Manifests API
  slug: cloud-foundry-manifests-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: Organization quotas are named sets of memory, log rate, service, and instance usage quotas.
  name: Cloud Foundry Organization Quotas API
  slug: cloud-foundry-organization-quotas-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: A package is an application’s ‘source code’; either raw bits for your application or a pointer to these bits.
  name: Cloud Foundry Packages API
  slug: cloud-foundry-packages-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: Processes define the runnable units of an app.
  name: Cloud Foundry Processes API
  slug: cloud-foundry-processes-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: Resource Matches are used to determine if a resource has been previously uploaded to the Cloud Controller.
  name: Cloud Foundry Resource Matches API
  slug: cloud-foundry-resource-matches-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: Revisions represent code used by an application at a specific time.
  name: Cloud Foundry Revisions API
  slug: cloud-foundry-revisions-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: Roles are used to control access to resources.
  name: Cloud Foundry Roles API
  slug: cloud-foundry-roles-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: Root API endpoints that provide entry points and API information.
  name: Cloud Foundry Root API
  slug: cloud-foundry-root-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: Routes are used to map a URL to an app.
  name: Cloud Foundry Routes API
  slug: cloud-foundry-routes-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: List the scaling history of an Application
  name: Cloud Foundry Scaling History API V1 API
  slug: cloud-foundry-scaling-history-api-v1-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: Security groups are used to control access to apps.
  name: Cloud Foundry Security Groups API
  slug: cloud-foundry-security-groups-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: Service brokers are used to manage services.
  name: Cloud Foundry Service Brokers API
  slug: cloud-foundry-service-brokers-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: Service credential bindings are used to bind a service instance to an app.
  name: Cloud Foundry Service Credential Bindings API
  slug: cloud-foundry-service-credential-bindings-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: Service offerings are services that are available to be used.
  name: Cloud Foundry Service Offerings API
  slug: cloud-foundry-service-offerings-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: Service plans are plans for a service.
  name: Cloud Foundry Service Plans API
  slug: cloud-foundry-service-plans-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: Service route bindings are used to bind a route to a service instance.
  name: Cloud Foundry Service Route Bindings API
  slug: cloud-foundry-service-route-bindings-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: Service usage events are a record of changes in the usage of services.
  name: Cloud Foundry Service Usage Events API
  slug: cloud-foundry-service-usage-events-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: The ServiceBindings API from Cloud Foundry — 2 operation(s) for servicebindings.
  name: Cloud Foundry Service Bindings API
  slug: cloud-foundry-servicebindings-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: Sidecars are used to run a process alongside an app.
  name: Cloud Foundry Sidecars API
  slug: cloud-foundry-sidecars-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: Space quotas are named sets of memory, log rate, service, and instance usage quotas.
  name: Cloud Foundry Space Quotas API
  slug: cloud-foundry-space-quotas-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: Stacks are used to specify the operating system and runtime environment for an app.
  name: Cloud Foundry Stacks API
  slug: cloud-foundry-stacks-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: Tasks are one-off commands that can be run against an app.
  name: Cloud Foundry Tasks API
  slug: cloud-foundry-tasks-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: Users are the users of the Cloud Foundry platform.
  name: Cloud Foundry Users API
  slug: cloud-foundry-users-api
artifact_total: 69
asyncapis:
- description: ''
  name: Cloud Foundry Event Surface
  slug: cloud-foundry-event-surface
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cloud Foundry Cloud Controller API v3 Apps API
  slug: open-cloud-foundry-apps-api
- collection_type: open
  name: Cloud Foundry Cloud Controller API v3 Apps Builds API
  slug: open-cloud-foundry-builds-api
- collection_type: open
  name: Apps Cloud Foundry Cloud Controller API V3 API
  slug: open-cloud-foundry-cloud-foundry-cloud-controller-api-v3-api
- collection_type: open
  name: Cloud Foundry Cloud Controller API v3 Apps Deployments API
  slug: open-cloud-foundry-deployments-api
- collection_type: open
  name: Cloud Foundry Cloud Controller API v3 Apps Jobs API
  slug: open-cloud-foundry-jobs-api
- collection_type: open
  name: Cloud Foundry Cloud Controller API v3 Apps Organizations API
  slug: open-cloud-foundry-organizations-api
- collection_type: open
  name: Cloud Foundry Cloud Controller API v3 Apps Service Instances API
  slug: open-cloud-foundry-service-instances-api
- collection_type: open
  name: Cloud Foundry Cloud Controller API v3 Apps Spaces API
  slug: open-cloud-foundry-spaces-api
- collection_type: open
  name: Cloud Foundry Cloud Controller API v3
  slug: open-cloud-foundry
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloud-foundry/refs/heads/main/scopes/cloud-foundry-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cloud-foundry-scopes.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloud-foundry/refs/heads/main/agentic-access/cloud-foundry-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cloud-foundry-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloud-foundry/refs/heads/main/security/cloud-foundry-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloud-foundry-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloud-foundry/refs/heads/main/authentication/cloud-foundry-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cloud-foundry-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloud-foundry
- group: company
  title: ''
  type: Website
  url: https://www.cloudfoundry.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cloudfoundry.org/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cloudfoundry
- group: other
  title: ''
  type: Foundation
  url: https://www.cloudfoundry.org/foundation/
- group: operate
  title: ''
  type: Community
  url: https://www.cloudfoundry.org/community/
- group: company
  title: ''
  type: Blog
  url: https://www.cloudfoundry.org/blog/
- group: other
  title: ''
  type: Events
  url: https://www.cloudfoundry.org/events/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.linuxfoundation.org/privacy
- group: other
  title: ''
  type: Trademark
  url: https://www.linuxfoundation.org/trademark-usage
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloud-foundry/refs/heads/main/json-ld/cloud-foundry-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloud-foundry-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloud-foundry/refs/heads/main/rules/cloud-foundry-rules.yml
  title: ''
  type: Spectral
  url: rules/cloud-foundry-rules.yml
- group: operate
  title: ''
  type: Slack
  url: https://cloudfoundry.slack.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cloudfoundry.org/terms/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.cloudfoundry.org/
- group: docs
  title: ''
  type: APIReference
  url: https://v3-apidocs.cloudfoundry.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cloudfoundry.org/cf-cli/getting-started.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloudfoundry
- group: operate
  title: ''
  type: Support
  url: https://www.cloudfoundry.org/community/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cloud-foundry/refs/heads/main/packages/cloud-foundry-packages.yml
  title: ''
  type: Packages
  url: packages/cloud-foundry-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cloud-foundry/refs/heads/main/packages/cloud-foundry-packages.yml
  title: ''
  type: SDKs
  url: packages/cloud-foundry-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cloud-foundry/refs/heads/main/cli/cloud-foundry-cli.yml
  title: ''
  type: CLI
  url: cli/cloud-foundry-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloud-foundry/refs/heads/main/llms/cloud-foundry-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloud-foundry-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloud-foundry/refs/heads/main/overlays/cloud-foundry-capi-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cloud-foundry-capi-v3-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloud-foundry/refs/heads/main/conformance/cloud-foundry-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloud-foundry-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloud-foundry/refs/heads/main/errors/cloud-foundry-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cloud-foundry-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloud-foundry/refs/heads/main/lifecycle/cloud-foundry-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cloud-foundry-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cloud-foundry/refs/heads/main/lifecycle/cloud-foundry-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/cloud-foundry-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloud-foundry/refs/heads/main/security/cloud-foundry-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cloud-foundry-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloud-foundry/refs/heads/main/security/cloud-foundry-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cloud-foundry-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloud-foundry/refs/heads/main/conventions/cloud-foundry-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cloud-foundry-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cloud-foundry/refs/heads/main/changelog/cloud-foundry-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cloud-foundry-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloud-foundry/refs/heads/main/data-model/cloud-foundry-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cloud-foundry-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloud-foundry/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cloud-foundry/refs/heads/main/plans/cloud-foundry-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cloud-foundry-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cloud-foundry/refs/heads/main/rate-limits/cloud-foundry-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cloud-foundry-rate-limits.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cloud-foundry/refs/heads/main/collections/cloud-foundry.postman_collection.json
  title: ''
  type: PostmanCollection
  url: collections/cloud-foundry.postman_collection.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cloud-foundry/refs/heads/main/collections/cloud-foundry.opencollection.json
  title: ''
  type: OpenCollection
  url: collections/cloud-foundry.opencollection.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloud-foundry/refs/heads/main/asyncapi/cloud-foundry-event-surface.yml
  title: ''
  type: EventSurface
  url: asyncapi/cloud-foundry-event-surface.yml
created: '2024-01-01'
description: Cloud Foundry is an open-source, multi-cloud Platform as a Service (PaaS) governed by the Cloud Foundry Foundation. It provides a developer-friendly application platform where operators push source code or container images and Cloud Foundry handles staging, routing, scaling, and lifecycle management. The CF API (api.cloudfoundry.org) is the primary control plane and is documented at v3.cloudfoundry.org/version/release-candidate. The ecosystem also includes the User Account and Authentication (UAA) OAuth 2.0 server, the Loggregator log and metric pipeline, the Diego container scheduler, the Open Service Broker API for marketplace services, and the Eirini Kubernetes-based scheduler.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloud-foundry.png
jsonld:
- class_count: 0
  name: Cloud Foundry Context
  property_count: 11
  slug: cloud-foundry-context
layout: provider
modified: '2026-09-05'
name: Cloud Foundry
nav: Providers
network: true
overview: 'Cloud Foundry publishes 46 APIs on the [APIs.io](https://apis.io/) network, including Apps API, Builds API, Deployments API, and 43 more. Tagged areas include Cloud Foundry Foundation, Containers, Multi-Cloud, Open-Source, and Platform-as-a-Service.


  The Cloud Foundry catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Cloud Foundry''s developer surface includes authentication, documentation, GitHub presence, engineering blog, API reference, getting-started guide, support, and 36 more developer resources.'
plans:
- name: Cloud Foundry Plans Pricing
  plan_count: 0
  slug: cloud-foundry-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Cloud Foundry Rate Limits
  slug: cloud-foundry-rate-limits
rules:
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Cloud Foundry API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 5
  slug: cloud-foundry-rules
scopes:
- name: Cloud Foundry Scopes
  scope_count: 7
  slug: cloud-foundry-scopes
  summary_line: 7 scopes · implicit
score:
  band: strong
  composite: 56.2
  coverage:
    artifact_dirs: 27
    catalog_earned: 50.0
    catalog_earned_first_party: 0.0
    catalog_gap: 65.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 72.7
    contract_quality: 72.0
    developer_ergonomics: 74.4
    discoverability: 51.9
    operational_transparency: 36.8
  previous_composite: 56.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 86.4
      derived: 0
      marker_coverage: 0.0
      total: 46
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://raw.githubusercontent.com/api-evangelist/cloud-foundry/refs/heads/main/screenshots/cloud-foundry-2026-06-20T174548.png
security:
- kind: authentication
  name: Cloud Foundry Authentication
  slug: cloud-foundry-authentication
  summary_line: http/mutualTLS/oauth2 · 4 schemes
- kind: domain-security
  name: Cloud Foundry Domain Security
  slug: cloud-foundry-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cloud Foundry Vulnerability Disclosure
  slug: cloud-foundry-vulnerability-disclosure
  summary_line: disclosure policy published
slug: cloud-foundry
tags:
- Cloud Foundry Foundation
- Containers
- Multi-Cloud
- Open-Source
- Platform-as-a-Service
- Platform
website: https://www.cloudfoundry.org/
---
