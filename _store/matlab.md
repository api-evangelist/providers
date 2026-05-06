---
name: MATLAB
description: APIs and integration points for MATLAB, a programming platform designed for engineers and scientists.
image: https://www.mathworks.com/etc/designs/mathworks/img/pic-header-mathworks-logo2.svg
url: https://www.mathworks.com
created: '2025'
modified: '2026-04-19'
apis:
  - name: MATLAB Engine API for Python
    description: Call MATLAB from Python, allowing Python programs to start MATLAB, execute MATLAB functions, and exchange data between Python and MATLAB.
    image: https://www.mathworks.com/etc/designs/mathworks/img/pic-header-mathworks-logo2.svg
    humanURL: https://www.mathworks.com/help/matlab/matlab-engine-for-python.html
    baseURL: https://www.mathworks.com/help/matlab/apiref
    tags:
      - Engine
      - Integration
      - Python
    properties:
      - type: Documentation
        url: https://www.mathworks.com/help/matlab/matlab-engine-for-python.html
      - type: GettingStarted
        url: https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html
      - type: GettingStarted
        url: https://www.mathworks.com/help/matlab/matlab_external/get-started-with-matlab-engine-for-python.html
      - type: APIReference
        url: https://www.mathworks.com/help/matlab/apiref/matlab.engine.matlabengine-class.html
      - type: SDK
        url: https://pypi.org/project/matlabengine/
      - type: GitHubRepository
        url: https://github.com/mathworks/matlab-engine-for-python
  - name: MATLAB Engine API for Java
    description: Execute MATLAB functions from Java programs and exchange data between Java and MATLAB.
    image: https://www.mathworks.com/etc/designs/mathworks/img/pic-header-mathworks-logo2.svg
    humanURL: https://www.mathworks.com/help/matlab/matlab-engine-api-for-java.html
    baseURL: https://www.mathworks.com/help/matlab/apiref
    tags:
      - Engine
      - Integration
      - Java
    properties:
      - type: Documentation
        url: https://www.mathworks.com/help/matlab/matlab-engine-api-for-java.html
      - type: APIReference
        url: https://www.mathworks.com/help/matlab/apiref/matlabengine-package.html
  - name: MATLAB Engine API for C++
    description: Call MATLAB from C++ programs with object-oriented programming support.
    image: https://www.mathworks.com/etc/designs/mathworks/img/pic-header-mathworks-logo2.svg
    humanURL: https://www.mathworks.com/help/matlab/matlab-engine-api-for-cpp.html
    baseURL: https://www.mathworks.com/help/matlab/apiref
    tags:
      - C++
      - Engine
      - Integration
    properties:
      - type: Documentation
        url: https://www.mathworks.com/help/matlab/matlab-engine-api-for-cpp.html
      - type: APIReference
        url: https://www.mathworks.com/help/matlab/apiref/matlab-engine-api-for-c++.html
      - type: Documentation
        url: https://www.mathworks.com/help/matlab/matlab_external/requirements-to-build-cpp-engine-programs.html
  - name: MATLAB Engine API for C and Fortran
    description: Call MATLAB from C and Fortran programs using the MATLAB engine library, enabling MATLAB as a computation engine for native applications.
    image: https://www.mathworks.com/etc/designs/mathworks/img/pic-header-mathworks-logo2.svg
    humanURL: https://www.mathworks.com/help/matlab/matlab_external/introducing-matlab-engine.html
    baseURL: https://www.mathworks.com/help/matlab/apiref
    tags:
      - C
      - Engine
      - Fortran
      - Integration
    properties:
      - type: Documentation
        url: https://www.mathworks.com/help/matlab/matlab_external/introducing-matlab-engine.html
      - type: Documentation
        url: https://www.mathworks.com/help/matlab/calling-matlab-engine-from-c-programs-1.html
      - type: Documentation
        url: https://www.mathworks.com/help/matlab/calling-matlab-engine-from-fortran-programs.html
      - type: APIReference
        url: https://www.mathworks.com/help/matlab/apiref/engine.html
      - type: Documentation
        url: https://www.mathworks.com/help/matlab/matlab_external/matlab-fortran-api-libraries.html
  - name: MATLAB Engine API for .NET
    description: Call MATLAB from .NET programming languages, enabling .NET programs to launch MATLAB, evaluate MATLAB functions with arguments, and exchange data synchronously or asynchronously.
    image: https://www.mathworks.com/etc/designs/mathworks/img/pic-header-mathworks-logo2.svg
    humanURL: https://www.mathworks.com/help/matlab/call-matlab-from-net.html
    baseURL: https://www.mathworks.com/help/matlab/apiref
    tags:
      - .NET
      - Engine
      - Integration
    properties:
      - type: Documentation
        url: https://www.mathworks.com/help/matlab/call-matlab-from-net.html
      - type: APIReference
        url: https://www.mathworks.com/help/matlab/apiref/mathworks.matlab.engine.matlabengine.html
      - type: Documentation
        url: https://www.mathworks.com/help/matlab/matlab_external/requirements-to-build-net-engine-programs.html
  - name: MATLAB RESTful Web Services
    description: Create and deploy RESTful web services from MATLAB functions using MATLAB Production Server.
    image: https://www.mathworks.com/etc/designs/mathworks/img/pic-header-mathworks-logo2.svg
    humanURL: https://www.mathworks.com/help/mps/restfuljson/creating-http-post-interface-to-restful-web-service.html
    baseURL: https://www.mathworks.com/products/matlab-production-server.html
    tags:
      - Production
      - REST
      - Web Services
    properties:
      - type: Documentation
        url: https://www.mathworks.com/help/mps/restfuljson/
      - type: Documentation
        url: https://www.mathworks.com/products/matlab-production-server.html
  - name: MATLAB Production Server RESTful API
    description: RESTful API for executing MATLAB functions on MATLAB Production Server, including function execution, discovery and diagnostics, and secure management of deployable archives.
    image: https://www.mathworks.com/etc/designs/mathworks/img/pic-header-mathworks-logo2.svg
    humanURL: https://www.mathworks.com/help/mps/restful-api-and-json.html
    baseURL: https://www.mathworks.com/help/mps
    tags:
      - Deployment
      - Enterprise
      - Production Server
      - REST
    properties:
      - type: Documentation
        url: https://www.mathworks.com/help/mps/restful-api-and-json.html
      - type: APIReference
        url: https://www.mathworks.com/help/mps/restfuljson/restful-api.html
      - type: APIReference
        url: https://www.mathworks.com/help/mps/restfuljson/restful-api-for-discovery-and-diagnostics.html
      - type: APIReference
        url: https://www.mathworks.com/help/mps/restfuljson/restful-api-for-deployable-archive-upload.html
      - type: Documentation
        url: https://www.mathworks.com/help/mps/client-programming.html
      - type: SDK
        url: https://www.mathworks.com/products/matlab-production-server/client-libraries.html
      - type: OpenAPI
        url: https://github.com/mathworks-ref-arch/openapi-productionserver
      - type: Documentation
        url: https://www.mathworks.com/help/mps/
  - name: MATLAB Web App Server
    description: Host MATLAB apps and Simulink simulations as interactive web apps, with support for authentication, role-based access, and server management via command-line interface.
    image: https://www.mathworks.com/etc/designs/mathworks/img/pic-header-mathworks-logo2.svg
    humanURL: https://www.mathworks.com/help/webappserver/index.html
    baseURL: https://www.mathworks.com/help/webappserver
    tags:
      - Deployment
      - Server
      - Web Apps
    properties:
      - type: Documentation
        url: https://www.mathworks.com/help/webappserver/index.html
      - type: Documentation
        url: https://www.mathworks.com/products/matlab-web-app-server.html
      - type: GettingStarted
        url: https://www.mathworks.com/help/webappserver/ug/set-up-matlab-web-app-server.html
      - type: Documentation
        url: https://www.mathworks.com/help/webappserver/server-management.html
      - type: APIReference
        url: https://www.mathworks.com/help/webappserver/ref/webappsconfig.html
  - name: MATLAB Data API for C++
    description: Work with MATLAB data types in C++ applications.
    image: https://www.mathworks.com/etc/designs/mathworks/img/pic-header-mathworks-logo2.svg
    humanURL: https://www.mathworks.com/help/matlab/matlab-data-api-for-c-plus-plus.html
    baseURL: https://www.mathworks.com/help/matlab/apiref
    tags:
      - C++
      - Data
      - Types
    properties:
      - type: Documentation
        url: https://www.mathworks.com/help/matlab/matlab-data-api-for-c-plus-plus.html
      - type: APIReference
        url: https://www.mathworks.com/help/matlab/apiref/matlab-data-api-for-c++.html
  - name: MATLAB HTTP Interface
    description: RESTful web services support for making HTTP requests from MATLAB.
    image: https://www.mathworks.com/etc/designs/mathworks/img/pic-header-mathworks-logo2.svg
    humanURL: https://www.mathworks.com/help/matlab/http-interface.html
    baseURL: https://www.mathworks.com/help/matlab
    tags:
      - Client
      - HTTP
      - REST
    properties:
      - type: Documentation
        url: https://www.mathworks.com/help/matlab/http-interface.html
      - type: CodeExamples
        url: https://www.mathworks.com/help/matlab/ref/webread.html
      - type: Documentation
        url: https://www.mathworks.com/help/matlab/web-services.html
  - name: MATLAB MEX API
    description: Build MEX functions that enable calling C, C++, and Fortran code from MATLAB, with support for both the C++ MEX API and the C Matrix API.
    image: https://www.mathworks.com/etc/designs/mathworks/img/pic-header-mathworks-logo2.svg
    humanURL: https://www.mathworks.com/help/matlab/call-mex-files-1.html
    baseURL: https://www.mathworks.com/help/matlab/apiref
    tags:
      - C
      - C++
      - Extensions
      - Fortran
      - MEX
    properties:
      - type: Documentation
        url: https://www.mathworks.com/help/matlab/call-mex-files-1.html
      - type: APIReference
        url: https://www.mathworks.com/help/matlab/matlab_external/cpp-mex-api.html
      - type: APIReference
        url: https://www.mathworks.com/help/matlab/matlab_external/c-mex-functions.html
      - type: APIReference
        url: https://www.mathworks.com/help/matlab/cc-mx-matrix-library.html
      - type: APIReference
        url: https://www.mathworks.com/help/matlab/ref/mex.html
  - name: MATLAB Compiler SDK API
    description: Build C/C++ shared libraries, .NET assemblies, Java classes, and Python packages from MATLAB programs for integration with custom applications.
    image: https://www.mathworks.com/etc/designs/mathworks/img/pic-header-mathworks-logo2.svg
    humanURL: https://www.mathworks.com/help/compiler_sdk/
    baseURL: https://www.mathworks.com/help/compiler_sdk
    tags:
      - Compiler
      - Deployment
      - Integration
      - SDK
    properties:
      - type: Documentation
        url: https://www.mathworks.com/help/compiler_sdk/
      - type: Documentation
        url: https://www.mathworks.com/products/matlab-compiler-sdk.html
      - type: GettingStarted
        url: https://www.mathworks.com/help/compiler_sdk/getting_started_with_compiler_sdk.html
      - type: APIReference
        url: https://www.mathworks.com/help/compiler_sdk/cxx/summary-of-sdk-cpp-apis.html
      - type: APIReference
        url: https://www.mathworks.com/help/compiler_sdk/dotnet/summary-of-matlab-compiler-sdk-dotnet-apis.html
      - type: Documentation
        url: https://www.mathworks.com/help/compiler_sdk/mps.html
  - name: ThingSpeak REST API
    description: IoT analytics platform REST API for reading and writing data to channels, creating and managing channels, and analyzing IoT data with MATLAB in the cloud.
    image: https://www.mathworks.com/etc/designs/mathworks/img/pic-header-mathworks-logo2.svg
    humanURL: https://www.mathworks.com/help/thingspeak/rest-api.html
    baseURL: https://api.thingspeak.com
    tags:
      - Analytics
      - Channels
      - IoT
      - REST
    properties:
      - type: Documentation
        url: https://www.mathworks.com/help/thingspeak/index.html
      - type: APIReference
        url: https://www.mathworks.com/help/thingspeak/rest-api.html
      - type: APIReference
        url: https://www.mathworks.com/help/thingspeak/channels-and-charts-api.html
      - type: Documentation
        url: https://www.mathworks.com/products/thingspeak.html
      - type: GitHubRepository
        url: https://github.com/mathworks/thingspeak-arduino
common:
  - type: Portal
    url: https://www.mathworks.com
  - type: Documentation
    url: https://www.mathworks.com/help/index.html
  - type: Pricing
    url: https://www.mathworks.com/pricing-licensing.html
  - type: Blog
    url: https://blogs.mathworks.com/
  - type: Community
    url: https://www.mathworks.com/matlabcentral/
  - type: Community
    url: https://www.mathworks.com/matlabcentral/answers/index
  - type: GitHubOrganization
    url: https://github.com/mathworks
  - type: StatusPage
    url: https://status.mathworks.com/
  - type: Support
    url: https://www.mathworks.com/support.html
  - type: Login
    url: https://www.mathworks.com/login
  - type: Features
    url: https://www.mathworks.com/products/matlab.html
  - type: UseCases
    url: https://www.mathworks.com/solutions.html
  - type: Integrations
    url: https://www.mathworks.com/products/connections.html
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - Data Analysis
  - Engineering
  - Machine Learning
  - Numerical Analysis
  - Scientific Computing
---
