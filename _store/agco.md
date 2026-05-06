---
aid: agco
url: https://raw.githubusercontent.com/api-evangelist/agco/refs/heads/main/apis.yml
apis:
  - aid: agco:agcommand-api
    name: AGCO AgCommand API
    tags:
      - Agriculture
      - Farm Equipment
      - IoT
      - Precision Farming
      - Telematics
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.agcocorp.com
    humanURL: https://get.agcoconnect.com/
    properties:
      - url: https://get.agcoconnect.com/
        type: Portal
      - url: https://github.com/agco/agco-json-api-profiles
        type: Documentation
      - url: openapi/agco-agcommand-api-openapi.yml
        type: OpenAPI
    description: The AGCO AgCommand API provides approved third-party developers and service providers with access to machine telemetry data from AGCO equipment. The API enables farming application developers to build management dashboards and mobile apps that access real-time machine data including location, performance metrics, and diagnostic information from AGCO Connect-ready machines. AGCO uses JSON API profiles for standardized filtering, search, and change events.
description: AGCO is a global leader in the design, manufacture, and distribution of agricultural machinery and precision ag technology. The AGCO AgCommand API enables approved third-party developers and service providers to access machine telemetry data, location tracking, and performance metrics from AGCO Connect-ready equipment including Fendt, Massey Ferguson, Challenger, and Valtra brands.
modified: '2026-04-19'
common:
  - type: Portal
    url: https://get.agcoconnect.com/
  - type: GettingStarted
    url: https://github.com/agco/agco-json-api-profiles
  - type: GitHubOrganization
    url: https://github.com/agco
  - type: TermsOfService
    url: https://www.agcocorp.com/legal/privacy-policy.html
  - type: Features
    data:
      - name: Machine Telematics
        description: Real-time access to machine performance data including engine speed, load, fuel consumption, and fault codes from AGCO Connect-ready equipment.
      - name: Fleet Location Tracking
        description: GPS-based machine location history enabling field work tracking and fleet management dashboards.
      - name: Diagnostic Fault Codes
        description: Remote access to machine diagnostic codes enabling proactive maintenance and reducing downtime.
      - name: JSON API Profiles
        description: Standardized filtering, search, and change event profiles for consistent API behavior across all resources.
      - name: Multi-Brand Coverage
        description: Single API access to data from Fendt, Massey Ferguson, Challenger, and Valtra agricultural equipment.
  - type: UseCases
    data:
      - name: Farm Management Dashboard
        description: Build web and mobile dashboards that display real-time machine location, performance, and fuel status for farm operators.
      - name: Predictive Maintenance
        description: Monitor machine fault codes and engine hours remotely to schedule preventive maintenance before failures occur.
      - name: Field Work Tracking
        description: Track machine location and activity data to document field operations, coverage areas, and productivity metrics.
      - name: Fuel Management
        description: Monitor fuel levels and consumption rates across a fleet to optimize refueling logistics and reduce costs.
      - name: Telematics Integration
        description: Integrate AGCO machine data into existing farm management or precision agriculture software platforms.
  - type: Integrations
    data:
      - name: Procore
        description: Integration of AGCO telematics data with Procore construction and project management workflows.
      - name: Precision Ag Software
        description: Integration with precision agriculture software platforms for combined field and machine data analysis.
  - type: JSONSchema
    url: json-schema/agco-location-schema.json
  - type: JSONSchema
    url: json-schema/agco-machine-schema.json
  - type: JSONSchema
    url: json-schema/agco-telemetry-schema.json
  - type: JSONStructure
    url: json-structure/agco-location-structure.json
  - type: JSONStructure
    url: json-structure/agco-machine-structure.json
  - type: JSONStructure
    url: json-structure/agco-telemetry-structure.json
  - type: JSON-LD
    url: json-ld/agco-telematics-context.jsonld
  - type: Example
    url: examples/agco-location-example.json
  - type: Example
    url: examples/agco-machine-example.json
  - type: Example
    url: examples/agco-telemetry-example.json
  - type: SpectralRules
    url: rules/agco-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/agco-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/precision-farming.yaml
---
