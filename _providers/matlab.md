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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.5
  scored_at: '2026-09-16'
api_count: 13
apis:
- description: Call MATLAB from Python, allowing Python programs to start MATLAB, execute MATLAB functions, and exchange data between Python and MATLAB.
  name: MATLAB Engine API for Python
  slug: matlab-engine-api-for-python
- description: Execute MATLAB functions from Java programs and exchange data between Java and MATLAB.
  name: MATLAB Engine API for Java
  slug: matlab-engine-api-for-java
- description: Call MATLAB from C++ programs with object-oriented programming support.
  name: MATLAB Engine API for C++
  slug: matlab-engine-api-for-c
- description: Call MATLAB from C and Fortran programs using the MATLAB engine library, enabling MATLAB as a computation engine for native applications.
  name: MATLAB Engine API for C and Fortran
  slug: matlab-engine-api-for-c-and-fortran
- description: Call MATLAB from .NET programming languages, enabling .NET programs to launch MATLAB, evaluate MATLAB functions with arguments, and exchange data synchronously or asynchronously.
  name: MATLAB Engine API for .NET
  slug: matlab-engine-api-for-net
- description: Create and deploy RESTful web services from MATLAB functions using MATLAB Production Server.
  name: MATLAB RESTful Web Services
  slug: matlab-restful-web-services
- description: RESTful API for executing MATLAB functions on MATLAB Production Server, including function execution, discovery and diagnostics, and secure management of deployable archives.
  name: MATLAB Production Server RESTful API
  slug: matlab-production-server-restful-api
- description: Host MATLAB apps and Simulink simulations as interactive web apps, with support for authentication, role-based access, and server management via command-line interface.
  name: MATLAB Web App Server
  slug: matlab-web-app-server
- description: Work with MATLAB data types in C++ applications.
  name: MATLAB Data API for C++
  slug: matlab-data-api-for-c
- description: RESTful web services support for making HTTP requests from MATLAB.
  name: MATLAB HTTP Interface
  slug: matlab-http-interface
- description: Build MEX functions that enable calling C, C++, and Fortran code from MATLAB, with support for both the C++ MEX API and the C Matrix API.
  name: MATLAB MEX API
  slug: matlab-mex-api
- description: Build C/C++ shared libraries, .NET assemblies, Java classes, and Python packages from MATLAB programs for integration with custom applications.
  name: MATLAB Compiler SDK API
  slug: matlab-compiler-sdk-api
- description: IoT analytics platform REST API for reading and writing data to channels, creating and managing channels, and analyzing IoT data with MATLAB in the cloud.
  name: ThingSpeak REST API
  slug: thingspeak-rest-api
artifact_total: 22
asyncapis:
- description: ''
  name: Matlab Thingspeak Events
  slug: matlab-thingspeak-events
common:
- group: company
  title: ''
  type: Website
  url: https://www.mathworks.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/matlab/refs/heads/main/security/matlab-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/matlab-vulnerability-disclosure.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/mathworks/matlab-engine-for-python/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/mathworks/matlab-engine-for-python/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/mathworks/matlab-engine-for-python/blob/R2026a/SECURITY.md
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/matlab/refs/heads/main/security/matlab-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/matlab-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-mathworks_2
- group: start
  title: ''
  type: Portal
  url: https://www.mathworks.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.mathworks.com/help/index.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mathworks.com/pricing-licensing.html
- group: company
  title: ''
  type: Blog
  url: https://blogs.mathworks.com/
- group: operate
  title: ''
  type: Community
  url: https://www.mathworks.com/matlabcentral/
- group: operate
  title: ''
  type: Community
  url: https://www.mathworks.com/matlabcentral/answers/index
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mathworks
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mathworks.com/
- group: operate
  title: ''
  type: Support
  url: https://www.mathworks.com/support.html
- group: start
  title: ''
  type: Login
  url: https://www.mathworks.com/login
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/matlab/refs/heads/main/packages/matlab-packages.yml
  title: ''
  type: Packages
  url: packages/matlab-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/matlab/refs/heads/main/packages/matlab-packages.yml
  title: ''
  type: SDKs
  url: packages/matlab-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/matlab/refs/heads/main/mcp/matlab-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/matlab-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/matlab/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/matlab/refs/heads/main/llms/matlab-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/matlab-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/matlab/refs/heads/main/well-known/matlab-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/matlab-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/matlab/refs/heads/main/well-known/matlab-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/matlab-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/matlab/refs/heads/main/security/matlab-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/matlab-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/matlab/refs/heads/main/security/matlab-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/matlab-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/matlab/refs/heads/main/security/matlab-trust-center.yml
  title: ''
  type: Compliance
  url: security/matlab-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/matlab/refs/heads/main/conformance/matlab-conformance.yml
  title: ''
  type: Conformance
  url: conformance/matlab-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/matlab/refs/heads/main/errors/matlab-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/matlab-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/matlab/refs/heads/main/lifecycle/matlab-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/matlab-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/matlab/refs/heads/main/lifecycle/matlab-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/matlab-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/matlab/refs/heads/main/authentication/matlab-authentication.yml
  title: ''
  type: Authentication
  url: authentication/matlab-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/matlab/refs/heads/main/conventions/matlab-conventions.yml
  title: ''
  type: Conventions
  url: conventions/matlab-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/matlab/refs/heads/main/changelog/matlab-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/matlab-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/matlab/refs/heads/main/cli/matlab-cli.yml
  title: ''
  type: CLI
  url: cli/matlab-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/matlab/refs/heads/main/asyncapi/matlab-thingspeak-events.yml
  title: ''
  type: Webhooks
  url: asyncapi/matlab-thingspeak-events.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/matlab/refs/heads/main/plans/matlab-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/matlab-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/matlab/refs/heads/main/rate-limits/matlab-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/matlab-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/matlab/refs/heads/main/finops/matlab-finops.yml
  title: ''
  type: FinOps
  url: finops/matlab-finops.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mathworks.com/matlabcentral/content/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mathworks.com/company/aboutus/policies_statements/privacy-policy.html
- group: start
  title: ''
  type: SignUp
  url: https://www.mathworks.com/mwaccount/register
created: '2025'
description: 'MATLAB is the MathWorks programming platform for engineers and scientists, and its interface surface is unusually split. Most of it is in-process language bindings — the MATLAB Engine APIs for Python, Java, C++, C, Fortran and .NET, the MEX API, the C++ Data API and the Compiler SDK — which embed MATLAB into other programs rather than exposing it over HTTP. Two surfaces are callable over the network: the ThingSpeak REST and MQTT APIs for IoT channel data, hosted by MathWorks, and the MATLAB Production Server RESTful API, which customers run themselves. On top of both sits a large first-party agent layer: the official MATLAB MCP Server and 212 published Agent Skills.'
finops:
- name: Matlab Finops
  service_category: API
  slug: matlab-finops
image: https://www.mathworks.com/etc/designs/mathworks/img/pic-header-mathworks-logo2.svg
layout: provider
mcp_servers:
- description: The official MathWorks MCP server. Lets an AI application start and quit MATLAB, write and run MATLAB code, run MATLAB unit tests, and statically analyse MATLAB code for style and correctness.
  name: MATLAB MCP Server
  slug: matlab-mcp-server
modified: '2026-09-14'
name: MATLAB
nav: Providers
network: true
overview: 'MATLAB publishes 1 API on the [APIs.io](https://apis.io/) network: Production Server RESTful API. Tagged areas include Data Analysis, Engineering, Machine-Learning, Numerical Analysis, and Scientific Computing.


  The MATLAB catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MATLAB''s developer surface includes developer portal, documentation, pricing, engineering blog, support, authentication, changelog, and 35 more developer resources.'
plans:
- name: Matlab Plans Pricing
  plan_count: 12
  slug: matlab-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 11
  name: Matlab Rate Limits
  slug: matlab-rate-limits
score:
  band: exemplar
  composite: 69.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 67.0
    catalog_earned_first_party: 24.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 93.4
    contract_governance: 4.5
    contract_quality: 48.1
    developer_ergonomics: 88.1
    discoverability: 88.9
    operational_transparency: 92.1
  previous_composite: 69.7
  provenance:
    conformance: derived
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/matlab/refs/heads/main/screenshots/matlab-2026-06-20T185035.png
security:
- kind: authentication
  name: Matlab Authentication
  slug: matlab-authentication
  summary_line: 7 schemes
- kind: domain-security
  name: Matlab Domain Security
  slug: matlab-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Matlab Vulnerability Disclosure
  slug: matlab-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Matlab Trust Center
  slug: matlab-trust-center
  summary_line: SOC 3, SOC 2 Type II, ISO 27001
slug: matlab
tags:
- Data Analysis
- Engineering
- Machine-Learning
- Numerical Analysis
- Scientific Computing
website: https://www.mathworks.com
---
