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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-12'
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
artifact_total: 17
common:
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
created: '2025'
description: APIs and integration points for MATLAB, a programming platform designed for engineers and scientists.
finops:
- name: Matlab Finops
  service_category: API
  slug: matlab-finops
image: https://www.mathworks.com/etc/designs/mathworks/img/pic-header-mathworks-logo2.svg
layout: provider
modified: '2026-04-19'
name: MATLAB
nav: Providers
network: true
overview: 'MATLAB publishes 1 API on the [APIs.io](https://apis.io/) network: Production Server RESTful API. Tagged areas include Data Analysis, Engineering, Machine Learning, Numerical Analysis, and Scientific Computing.


  MATLAB''s developer surface includes developer portal, documentation, pricing, engineering blog, support, and 10 more developer resources.'
plans:
- name: Matlab Plans Pricing
  plan_count: 3
  slug: matlab-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 5
  name: Matlab Rate Limits
  slug: matlab-rate-limits
score:
  band: thin
  composite: 35.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 32.3
    developer_ergonomics: 23.9
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 55.3
  previous_composite: 35.2
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/matlab/refs/heads/main/screenshots/matlab-2026-06-20T185035.png
security:
- kind: domain-security
  name: Matlab Domain Security
  slug: matlab-domain-security
  summary_line: TLSv1.3 · DMARC
slug: matlab
tags:
- Data Analysis
- Engineering
- Machine Learning
- Numerical Analysis
- Scientific Computing
website: https://www.mathworks.com
---
