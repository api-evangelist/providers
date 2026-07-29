---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 119
  human_in_the_loop: 20
  name: Agstack Agentic Access
  operation_count: 191
  slug: agstack-agentic-access
  summary_line: 191 operations · 119 acting · 20 human-in-the-loop
api_count: 7
apis:
- description: The api API from AgStack Foundation — 57 operation(s) for api.
  name: AgStack Foundation api API
  slug: agstack-api-api
- description: The Auth API from AgStack Foundation — 2 operation(s) for auth.
  name: AgStack Foundation Auth API
  slug: agstack-auth-api
- description: The Authentication API from AgStack Foundation — 1 operation(s) for authentication.
  name: AgStack Foundation Authentication API
  slug: agstack-authentication-api
- description: The Data API from AgStack Foundation — 6 operation(s) for data.
  name: AgStack Foundation Data API
  slug: agstack-data-api
- description: The Field Registration (POST) API from AgStack Foundation — 4 operation(s) for field registration (post).
  name: AgStack Foundation Field Registration (POST) API
  slug: agstack-field-registration-post-api
- description: The Field Retrieval & Queries API from AgStack Foundation — 4 operation(s) for field retrieval & queries.
  name: AgStack Foundation Field Retrieval & Queries API
  slug: agstack-field-retrieval-queries-api
- description: The Linkeddata API from AgStack Foundation — 5 operation(s) for linkeddata.
  name: AgStack Foundation Linkeddata API
  slug: agstack-linkeddata-api
artifact_total: 259
collections:
- collection_type: open
  name: AgStack Asset Registry API
  slug: open-agstack-asset-registry
- collection_type: open
  name: OpenAgri Farm Calendar API
  slug: open-agstack-openagri-farm-calendar
- collection_type: open
  name: OpenAgri Weather service
  slug: open-agstack-openagri-weather-service
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/agstack-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agstack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agstack-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://agstack.org/feed/
- group: start
  title: ''
  type: Portal
  url: https://agstack.org/
- group: docs
  title: ''
  type: Documentation
  url: https://agstack.org/projects/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agstack
- group: company
  title: ''
  type: About
  url: https://agstack.org/about/
- group: company
  title: Linux Foundation AI and Data
  type: About
  url: https://lfaidata.foundation/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/agstack-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/agstack-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/agstack-vocabulary.yaml
created: '2026-03-16'
description: AgStack Foundation is a Linux Foundation project providing open-source digital infrastructure for the agriculture sector. Key projects include the Asset Registry (global field boundary registration with unique geo IDs), the OpenAgri Weather Service (agricultural weather forecasts, THI, spray conditions, UAV flight forecasts), and the OpenAgri Farm Calendar (farm operation recording with JSON-LD/OCSM linked data support). AgStack tools support EUDR compliance, precision agriculture, and interoperability across the agtech ecosystem through the OpenAgri Common Semantic Model.
examples:
- key_count: 4
  name: Agstack Asset Registry Bulkpointresult Example
  slug: agstack-asset-registry-bulkpointresult-example
- key_count: 2
  name: Agstack Asset Registry Geojsonfeaturecollection Example
  slug: agstack-asset-registry-geojsonfeaturecollection-example
- key_count: 4
  name: Agstack Asset Registry Registerfieldwktrequest Example
  slug: agstack-asset-registry-registerfieldwktrequest-example
- key_count: 3
  name: Agstack Openagri Farm Calendar Addrawmaterialcompostquantity Example
  slug: agstack-openagri-farm-calendar-addrawmaterialcompostquantity-example
- key_count: 10
  name: Agstack Openagri Farm Calendar Addrawmaterialoperation Example
  slug: agstack-openagri-farm-calendar-addrawmaterialoperation-example
- key_count: 6
  name: Agstack Openagri Farm Calendar Addressfield Example
  slug: agstack-openagri-farm-calendar-addressfield-example
- key_count: 12
  name: Agstack Openagri Farm Calendar Agriculturalmachine Example
  slug: agstack-openagri-farm-calendar-agriculturalmachine-example
- key_count: 11
  name: Agstack Openagri Farm Calendar Alert Example
  slug: agstack-openagri-farm-calendar-alert-example
- key_count: 2
  name: Agstack Openagri Farm Calendar Appliedammountfield Example
  slug: agstack-openagri-farm-calendar-appliedammountfield-example
- key_count: 12
  name: Agstack Openagri Farm Calendar Compostoperation Example
  slug: agstack-openagri-farm-calendar-compostoperation-example
- key_count: 9
  name: Agstack Openagri Farm Calendar Compostturningoperation Example
  slug: agstack-openagri-farm-calendar-compostturningoperation-example
- key_count: 2
  name: Agstack Openagri Farm Calendar Contactpersonfield Example
  slug: agstack-openagri-farm-calendar-contactpersonfield-example
- key_count: 11
  name: Agstack Openagri Farm Calendar Cropgrowthstageobservation Example
  slug: agstack-openagri-farm-calendar-cropgrowthstageobservation-example
- key_count: 11
  name: Agstack Openagri Farm Calendar Cropprotectionoperation Example
  slug: agstack-openagri-farm-calendar-cropprotectionoperation-example
- key_count: 2
  name: Agstack Openagri Farm Calendar Cropspeciesserializerfield Example
  slug: agstack-openagri-farm-calendar-cropspeciesserializerfield-example
- key_count: 11
  name: Agstack Openagri Farm Calendar Cropstressindicatorobservation Example
  slug: agstack-openagri-farm-calendar-cropstressindicatorobservation-example
- key_count: 11
  name: Agstack Openagri Farm Calendar Diseasedetectionobservation Example
  slug: agstack-openagri-farm-calendar-diseasedetectionobservation-example
- key_count: 13
  name: Agstack Openagri Farm Calendar Farm Example
  slug: agstack-openagri-farm-calendar-farm-example
- key_count: 15
  name: Agstack Openagri Farm Calendar Farmanimal Example
  slug: agstack-openagri-farm-calendar-farmanimal-example
- key_count: 1
  name: Agstack Openagri Farm Calendar Farmanimalgroupserializerfield Example
  slug: agstack-openagri-farm-calendar-farmanimalgroupserializerfield-example
- key_count: 9
  name: Agstack Openagri Farm Calendar Farmcalendaractivity Example
  slug: agstack-openagri-farm-calendar-farmcalendaractivity-example
- key_count: 8
  name: Agstack Openagri Farm Calendar Farmcalendaractivitytype Example
  slug: agstack-openagri-farm-calendar-farmcalendaractivitytype-example
- key_count: 10
  name: Agstack Openagri Farm Calendar Farmcrop Example
  slug: agstack-openagri-farm-calendar-farmcrop-example
- key_count: 25
  name: Agstack Openagri Farm Calendar Farmparcel Example
  slug: agstack-openagri-farm-calendar-farmparcel-example
- key_count: 12
  name: Agstack Openagri Farm Calendar Fertilizationoperation Example
  slug: agstack-openagri-farm-calendar-fertilizationoperation-example
- key_count: 12
  name: Agstack Openagri Farm Calendar Fertilizer Example
  slug: agstack-openagri-farm-calendar-fertilizer-example
- key_count: 8
  name: Agstack Openagri Farm Calendar Genericfarmasset Example
  slug: agstack-openagri-farm-calendar-genericfarmasset-example
- key_count: 2
  name: Agstack Openagri Farm Calendar Genericquantityvaluefield Example
  slug: agstack-openagri-farm-calendar-genericquantityvaluefield-example
- key_count: 1
  name: Agstack Openagri Farm Calendar Geometryserializerfield Example
  slug: agstack-openagri-farm-calendar-geometryserializerfield-example
- key_count: 11
  name: Agstack Openagri Farm Calendar Irrigationoperation Example
  slug: agstack-openagri-farm-calendar-irrigationoperation-example
- key_count: 2
  name: Agstack Openagri Farm Calendar Locationserializerfield Example
  slug: agstack-openagri-farm-calendar-locationserializerfield-example
- key_count: 1
  name: Agstack Openagri Farm Calendar Madebysensorfield Example
  slug: agstack-openagri-farm-calendar-madebysensorfield-example
- key_count: 10
  name: Agstack Openagri Farm Calendar Observation Example
  slug: agstack-openagri-farm-calendar-observation-example
- key_count: 2
  name: Agstack Openagri Farm Calendar Observationquantityvaluefield Example
  slug: agstack-openagri-farm-calendar-observationquantityvaluefield-example
- key_count: 10
  name: Agstack Openagri Farm Calendar Patchedaddrawmaterialoperation Example
  slug: agstack-openagri-farm-calendar-patchedaddrawmaterialoperation-example
- key_count: 12
  name: Agstack Openagri Farm Calendar Patchedagriculturalmachine Example
  slug: agstack-openagri-farm-calendar-patchedagriculturalmachine-example
- key_count: 11
  name: Agstack Openagri Farm Calendar Patchedalert Example
  slug: agstack-openagri-farm-calendar-patchedalert-example
- key_count: 12
  name: Agstack Openagri Farm Calendar Patchedcompostoperation Example
  slug: agstack-openagri-farm-calendar-patchedcompostoperation-example
- key_count: 9
  name: Agstack Openagri Farm Calendar Patchedcompostturningoperation Example
  slug: agstack-openagri-farm-calendar-patchedcompostturningoperation-example
- key_count: 11
  name: Agstack Openagri Farm Calendar Patchedcropgrowthstageobservation Example
  slug: agstack-openagri-farm-calendar-patchedcropgrowthstageobservation-example
- key_count: 11
  name: Agstack Openagri Farm Calendar Patchedcropprotectionoperation Example
  slug: agstack-openagri-farm-calendar-patchedcropprotectionoperation-example
- key_count: 11
  name: Agstack Openagri Farm Calendar Patchedcropstressindicatorobservation Example
  slug: agstack-openagri-farm-calendar-patchedcropstressindicatorobservation-example
- key_count: 11
  name: Agstack Openagri Farm Calendar Patcheddiseasedetectionobservation Example
  slug: agstack-openagri-farm-calendar-patcheddiseasedetectionobservation-example
- key_count: 13
  name: Agstack Openagri Farm Calendar Patchedfarm Example
  slug: agstack-openagri-farm-calendar-patchedfarm-example
- key_count: 15
  name: Agstack Openagri Farm Calendar Patchedfarmanimal Example
  slug: agstack-openagri-farm-calendar-patchedfarmanimal-example
- key_count: 9
  name: Agstack Openagri Farm Calendar Patchedfarmcalendaractivity Example
  slug: agstack-openagri-farm-calendar-patchedfarmcalendaractivity-example
- key_count: 8
  name: Agstack Openagri Farm Calendar Patchedfarmcalendaractivitytype Example
  slug: agstack-openagri-farm-calendar-patchedfarmcalendaractivitytype-example
- key_count: 10
  name: Agstack Openagri Farm Calendar Patchedfarmcrop Example
  slug: agstack-openagri-farm-calendar-patchedfarmcrop-example
- key_count: 25
  name: Agstack Openagri Farm Calendar Patchedfarmparcel Example
  slug: agstack-openagri-farm-calendar-patchedfarmparcel-example
- key_count: 12
  name: Agstack Openagri Farm Calendar Patchedfertilizationoperation Example
  slug: agstack-openagri-farm-calendar-patchedfertilizationoperation-example
- key_count: 12
  name: Agstack Openagri Farm Calendar Patchedfertilizer Example
  slug: agstack-openagri-farm-calendar-patchedfertilizer-example
- key_count: 8
  name: Agstack Openagri Farm Calendar Patchedgenericfarmasset Example
  slug: agstack-openagri-farm-calendar-patchedgenericfarmasset-example
- key_count: 11
  name: Agstack Openagri Farm Calendar Patchedirrigationoperation Example
  slug: agstack-openagri-farm-calendar-patchedirrigationoperation-example
- key_count: 10
  name: Agstack Openagri Farm Calendar Patchedobservation Example
  slug: agstack-openagri-farm-calendar-patchedobservation-example
- key_count: 12
  name: Agstack Openagri Farm Calendar Patchedpesticide Example
  slug: agstack-openagri-farm-calendar-patchedpesticide-example
- key_count: 12
  name: Agstack Openagri Farm Calendar Patchedsprayingrecommendationobservation Example
  slug: agstack-openagri-farm-calendar-patchedsprayingrecommendationobservation-example
- key_count: 11
  name: Agstack Openagri Farm Calendar Patchedvigorestimationobservation Example
  slug: agstack-openagri-farm-calendar-patchedvigorestimationobservation-example
- key_count: 11
  name: Agstack Openagri Farm Calendar Patchedyieldpredictionobservation Example
  slug: agstack-openagri-farm-calendar-patchedyieldpredictionobservation-example
- key_count: 12
  name: Agstack Openagri Farm Calendar Pesticide Example
  slug: agstack-openagri-farm-calendar-pesticide-example
- key_count: 12
  name: Agstack Openagri Farm Calendar Sprayingrecommendationobservation Example
  slug: agstack-openagri-farm-calendar-sprayingrecommendationobservation-example
- key_count: 11
  name: Agstack Openagri Farm Calendar Vigorestimationobservation Example
  slug: agstack-openagri-farm-calendar-vigorestimationobservation-example
- key_count: 11
  name: Agstack Openagri Farm Calendar Yieldpredictionobservation Example
  slug: agstack-openagri-farm-calendar-yieldpredictionobservation-example
- key_count: 1
  name: Agstack Openagri Weather Service Authtoken Example
  slug: agstack-openagri-weather-service-authtoken-example
- key_count: 6
  name: Agstack Openagri Weather Service Body Token Auth Token Post Example
  slug: agstack-openagri-weather-service-body-token-auth-token-post-example
- key_count: 6
  name: Agstack Openagri Weather Service Flightstatusforecastresponse Example
  slug: agstack-openagri-weather-service-flightstatusforecastresponse-example
- key_count: 2
  name: Agstack Openagri Weather Service Geojsonout Example
  slug: agstack-openagri-weather-service-geojsonout-example
- key_count: 1
  name: Agstack Openagri Weather Service Httpvalidationerror Example
  slug: agstack-openagri-weather-service-httpvalidationerror-example
- key_count: 2
  name: Agstack Openagri Weather Service Jsonldgraph Example
  slug: agstack-openagri-weather-service-jsonldgraph-example
- key_count: 1
  name: Agstack Openagri Weather Service Pointout Example
  slug: agstack-openagri-weather-service-pointout-example
- key_count: 6
  name: Agstack Openagri Weather Service Predictionout Example
  slug: agstack-openagri-weather-service-predictionout-example
- key_count: 5
  name: Agstack Openagri Weather Service Sprayforecastresponse Example
  slug: agstack-openagri-weather-service-sprayforecastresponse-example
- key_count: 3
  name: Agstack Openagri Weather Service Thidataout Example
  slug: agstack-openagri-weather-service-thidataout-example
- key_count: 3
  name: Agstack Openagri Weather Service Validationerror Example
  slug: agstack-openagri-weather-service-validationerror-example
- key_count: 3
  name: Agstack Openagri Weather Service Weatherdataout Example
  slug: agstack-openagri-weather-service-weatherdataout-example
features:
- description: Global registry for agricultural field boundaries — submit WKT or GeoJSON geometry, receive a permanent unique 16-character geo ID
  name: Field Boundary Registry
- description: 5-day weather forecasts, current conditions, and agricultural indicators including THI, spray conditions, and UAV flight suitability
  name: Agricultural Weather Intelligence
- description: Record and manage farm operations (planting, irrigation, spraying, harvesting) with linked data (JSON-LD/OCSM) output
  name: Digital Farm Calendar
- description: All APIs support JSON-LD output conforming to the OpenAgri Common Semantic Model (OCSM) for semantic interoperability
  name: Linked Data Support
- description: Tools for EU Deforestation Regulation compliance — field boundary registration and supply chain traceability via INATrace
  name: EUDR Compliance Support
- description: Evapotranspiration (ETo) calculations and soil moisture analysis for data-driven irrigation decisions
  name: Irrigation Management
- description: All tools are Apache-2.0 licensed, Docker-ready, and deployable on any cloud or on-premises infrastructure
  name: Open Source Infrastructure
finops:
- name: Agstack Finops
  service_category: API
  slug: agstack-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agstack.png
integrations:
- description: Weather data source for current conditions and forecasts used by the OpenAgri Weather Service
  name: OpenWeatherMap
- description: EU Horizon Europe project (Grant No. 101134083) that funds and drives the OpenAgri microservices ecosystem
  name: OpenAgri
- description: OpenAgri Common Semantic Model — linked data vocabulary for agricultural interoperability used across all OpenAgri APIs
  name: OCSM
- description: Open-source blockchain-based track and trace system for agricultural supply chains
  name: INATrace
- description: TechnoServe Labs mobile and web application for EUDR compliance field data collection integrated with the asset registry
  name: TerraTrac
json_schemas:
- name: BulkPointResult
  property_count: 4
  slug: agstack-asset-registry-bulkpointresult
- name: GeoJSONFeatureCollection
  property_count: 2
  slug: agstack-asset-registry-geojsonfeaturecollection
- name: RegisterFieldWKTRequest
  property_count: 4
  slug: agstack-asset-registry-registerfieldwktrequest
- name: AddRawMaterialCompostQuantity
  property_count: 3
  slug: agstack-openagri-farm-calendar-addrawmaterialcompostquantity
- name: AddRawMaterialOperation
  property_count: 10
  slug: agstack-openagri-farm-calendar-addrawmaterialoperation
- name: AddressField
  property_count: 6
  slug: agstack-openagri-farm-calendar-addressfield
- name: AgriculturalMachine
  property_count: 12
  slug: agstack-openagri-farm-calendar-agriculturalmachine
- name: Alert
  property_count: 11
  slug: agstack-openagri-farm-calendar-alert
- name: AppliedAmmountField
  property_count: 2
  slug: agstack-openagri-farm-calendar-appliedammountfield
- name: CompostOperation
  property_count: 12
  slug: agstack-openagri-farm-calendar-compostoperation
- name: CompostTurningOperation
  property_count: 9
  slug: agstack-openagri-farm-calendar-compostturningoperation
- name: ContactPersonField
  property_count: 2
  slug: agstack-openagri-farm-calendar-contactpersonfield
- name: CropGrowthStageObservation
  property_count: 11
  slug: agstack-openagri-farm-calendar-cropgrowthstageobservation
- name: CropProtectionOperation
  property_count: 11
  slug: agstack-openagri-farm-calendar-cropprotectionoperation
- name: CropSpeciesSerializerField
  property_count: 2
  slug: agstack-openagri-farm-calendar-cropspeciesserializerfield
- name: CropStressIndicatorObservation
  property_count: 11
  slug: agstack-openagri-farm-calendar-cropstressindicatorobservation
- name: DiseaseDetectionObservation
  property_count: 11
  slug: agstack-openagri-farm-calendar-diseasedetectionobservation
- name: Farm
  property_count: 13
  slug: agstack-openagri-farm-calendar-farm
- name: FarmAnimal
  property_count: 15
  slug: agstack-openagri-farm-calendar-farmanimal
- name: FarmAnimalGroupSerializerField
  property_count: 1
  slug: agstack-openagri-farm-calendar-farmanimalgroupserializerfield
- name: FarmCalendarActivity
  property_count: 9
  slug: agstack-openagri-farm-calendar-farmcalendaractivity
- name: FarmCalendarActivityType
  property_count: 8
  slug: agstack-openagri-farm-calendar-farmcalendaractivitytype
- name: FarmCrop
  property_count: 10
  slug: agstack-openagri-farm-calendar-farmcrop
- name: FarmParcel
  property_count: 25
  slug: agstack-openagri-farm-calendar-farmparcel
- name: FertilizationOperation
  property_count: 12
  slug: agstack-openagri-farm-calendar-fertilizationoperation
- name: Fertilizer
  property_count: 12
  slug: agstack-openagri-farm-calendar-fertilizer
- name: GenericFarmAsset
  property_count: 8
  slug: agstack-openagri-farm-calendar-genericfarmasset
- name: GenericQuantityValueField
  property_count: 2
  slug: agstack-openagri-farm-calendar-genericquantityvaluefield
- name: GeometrySerializerField
  property_count: 1
  slug: agstack-openagri-farm-calendar-geometryserializerfield
- name: IrrigationOperation
  property_count: 11
  slug: agstack-openagri-farm-calendar-irrigationoperation
- name: LocationSerializerField
  property_count: 2
  slug: agstack-openagri-farm-calendar-locationserializerfield
- name: MadeBySensorField
  property_count: 1
  slug: agstack-openagri-farm-calendar-madebysensorfield
- name: Observation
  property_count: 10
  slug: agstack-openagri-farm-calendar-observation
- name: ObservationQuantityValueField
  property_count: 2
  slug: agstack-openagri-farm-calendar-observationquantityvaluefield
- name: PatchedAddRawMaterialOperation
  property_count: 10
  slug: agstack-openagri-farm-calendar-patchedaddrawmaterialoperation
- name: PatchedAgriculturalMachine
  property_count: 12
  slug: agstack-openagri-farm-calendar-patchedagriculturalmachine
- name: PatchedAlert
  property_count: 11
  slug: agstack-openagri-farm-calendar-patchedalert
- name: PatchedCompostOperation
  property_count: 12
  slug: agstack-openagri-farm-calendar-patchedcompostoperation
- name: PatchedCompostTurningOperation
  property_count: 9
  slug: agstack-openagri-farm-calendar-patchedcompostturningoperation
- name: PatchedCropGrowthStageObservation
  property_count: 11
  slug: agstack-openagri-farm-calendar-patchedcropgrowthstageobservation
- name: PatchedCropProtectionOperation
  property_count: 11
  slug: agstack-openagri-farm-calendar-patchedcropprotectionoperation
- name: PatchedCropStressIndicatorObservation
  property_count: 11
  slug: agstack-openagri-farm-calendar-patchedcropstressindicatorobservation
- name: PatchedDiseaseDetectionObservation
  property_count: 11
  slug: agstack-openagri-farm-calendar-patcheddiseasedetectionobservation
- name: PatchedFarm
  property_count: 13
  slug: agstack-openagri-farm-calendar-patchedfarm
- name: PatchedFarmAnimal
  property_count: 15
  slug: agstack-openagri-farm-calendar-patchedfarmanimal
- name: PatchedFarmCalendarActivity
  property_count: 9
  slug: agstack-openagri-farm-calendar-patchedfarmcalendaractivity
- name: PatchedFarmCalendarActivityType
  property_count: 8
  slug: agstack-openagri-farm-calendar-patchedfarmcalendaractivitytype
- name: PatchedFarmCrop
  property_count: 10
  slug: agstack-openagri-farm-calendar-patchedfarmcrop
- name: PatchedFarmParcel
  property_count: 25
  slug: agstack-openagri-farm-calendar-patchedfarmparcel
- name: PatchedFertilizationOperation
  property_count: 12
  slug: agstack-openagri-farm-calendar-patchedfertilizationoperation
- name: PatchedFertilizer
  property_count: 12
  slug: agstack-openagri-farm-calendar-patchedfertilizer
- name: PatchedGenericFarmAsset
  property_count: 8
  slug: agstack-openagri-farm-calendar-patchedgenericfarmasset
- name: PatchedIrrigationOperation
  property_count: 11
  slug: agstack-openagri-farm-calendar-patchedirrigationoperation
- name: PatchedObservation
  property_count: 10
  slug: agstack-openagri-farm-calendar-patchedobservation
- name: PatchedPesticide
  property_count: 12
  slug: agstack-openagri-farm-calendar-patchedpesticide
- name: PatchedSprayingRecommendationObservation
  property_count: 12
  slug: agstack-openagri-farm-calendar-patchedsprayingrecommendationobservation
- name: PatchedVigorEstimationObservation
  property_count: 11
  slug: agstack-openagri-farm-calendar-patchedvigorestimationobservation
- name: PatchedYieldPredictionObservation
  property_count: 11
  slug: agstack-openagri-farm-calendar-patchedyieldpredictionobservation
- name: Pesticide
  property_count: 12
  slug: agstack-openagri-farm-calendar-pesticide
- name: SprayingRecommendationObservation
  property_count: 12
  slug: agstack-openagri-farm-calendar-sprayingrecommendationobservation
- name: VigorEstimationObservation
  property_count: 11
  slug: agstack-openagri-farm-calendar-vigorestimationobservation
- name: YieldPredictionObservation
  property_count: 11
  slug: agstack-openagri-farm-calendar-yieldpredictionobservation
- name: AuthToken
  property_count: 1
  slug: agstack-openagri-weather-service-authtoken
- name: Body_token_auth_token_post
  property_count: 6
  slug: agstack-openagri-weather-service-body-token-auth-token-post
- name: FlightStatusForecastResponse
  property_count: 6
  slug: agstack-openagri-weather-service-flightstatusforecastresponse
- name: GeoJSONOut
  property_count: 2
  slug: agstack-openagri-weather-service-geojsonout
- name: HTTPValidationError
  property_count: 1
  slug: agstack-openagri-weather-service-httpvalidationerror
- name: JSONLDGraph
  property_count: 2
  slug: agstack-openagri-weather-service-jsonldgraph
- name: PointOut
  property_count: 1
  slug: agstack-openagri-weather-service-pointout
- name: PredictionOut
  property_count: 6
  slug: agstack-openagri-weather-service-predictionout
- name: SprayForecastResponse
  property_count: 5
  slug: agstack-openagri-weather-service-sprayforecastresponse
- name: THIDataOut
  property_count: 3
  slug: agstack-openagri-weather-service-thidataout
- name: ValidationError
  property_count: 3
  slug: agstack-openagri-weather-service-validationerror
- name: WeatherDataOut
  property_count: 3
  slug: agstack-openagri-weather-service-weatherdataout
json_structures:
- name: Agstack Asset Registry Bulkpointresult Structure
  property_count: 0
  slug: agstack-asset-registry-bulkpointresult-structure
- name: Agstack Asset Registry Geojsonfeaturecollection Structure
  property_count: 0
  slug: agstack-asset-registry-geojsonfeaturecollection-structure
- name: Agstack Asset Registry Registerfieldwktrequest Structure
  property_count: 0
  slug: agstack-asset-registry-registerfieldwktrequest-structure
- name: Agstack Openagri Farm Calendar Addrawmaterialcompostquantity Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-addrawmaterialcompostquantity-structure
- name: Agstack Openagri Farm Calendar Addrawmaterialoperation Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-addrawmaterialoperation-structure
- name: Agstack Openagri Farm Calendar Addressfield Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-addressfield-structure
- name: Agstack Openagri Farm Calendar Agriculturalmachine Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-agriculturalmachine-structure
- name: Agstack Openagri Farm Calendar Alert Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-alert-structure
- name: Agstack Openagri Farm Calendar Appliedammountfield Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-appliedammountfield-structure
- name: Agstack Openagri Farm Calendar Compostoperation Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-compostoperation-structure
- name: Agstack Openagri Farm Calendar Compostturningoperation Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-compostturningoperation-structure
- name: Agstack Openagri Farm Calendar Contactpersonfield Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-contactpersonfield-structure
- name: Agstack Openagri Farm Calendar Cropgrowthstageobservation Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-cropgrowthstageobservation-structure
- name: Agstack Openagri Farm Calendar Cropprotectionoperation Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-cropprotectionoperation-structure
- name: Agstack Openagri Farm Calendar Cropspeciesserializerfield Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-cropspeciesserializerfield-structure
- name: Agstack Openagri Farm Calendar Cropstressindicatorobservation Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-cropstressindicatorobservation-structure
- name: Agstack Openagri Farm Calendar Diseasedetectionobservation Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-diseasedetectionobservation-structure
- name: Agstack Openagri Farm Calendar Farm Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-farm-structure
- name: Agstack Openagri Farm Calendar Farmanimal Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-farmanimal-structure
- name: Agstack Openagri Farm Calendar Farmanimalgroupserializerfield Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-farmanimalgroupserializerfield-structure
- name: Agstack Openagri Farm Calendar Farmcalendaractivity Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-farmcalendaractivity-structure
- name: Agstack Openagri Farm Calendar Farmcalendaractivitytype Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-farmcalendaractivitytype-structure
- name: Agstack Openagri Farm Calendar Farmcrop Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-farmcrop-structure
- name: Agstack Openagri Farm Calendar Farmparcel Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-farmparcel-structure
- name: Agstack Openagri Farm Calendar Fertilizationoperation Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-fertilizationoperation-structure
- name: Agstack Openagri Farm Calendar Fertilizer Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-fertilizer-structure
- name: Agstack Openagri Farm Calendar Genericfarmasset Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-genericfarmasset-structure
- name: Agstack Openagri Farm Calendar Genericquantityvaluefield Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-genericquantityvaluefield-structure
- name: Agstack Openagri Farm Calendar Geometryserializerfield Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-geometryserializerfield-structure
- name: Agstack Openagri Farm Calendar Irrigationoperation Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-irrigationoperation-structure
- name: Agstack Openagri Farm Calendar Locationserializerfield Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-locationserializerfield-structure
- name: Agstack Openagri Farm Calendar Madebysensorfield Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-madebysensorfield-structure
- name: Agstack Openagri Farm Calendar Observation Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-observation-structure
- name: Agstack Openagri Farm Calendar Observationquantityvaluefield Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-observationquantityvaluefield-structure
- name: Agstack Openagri Farm Calendar Patchedaddrawmaterialoperation Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-patchedaddrawmaterialoperation-structure
- name: Agstack Openagri Farm Calendar Patchedagriculturalmachine Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-patchedagriculturalmachine-structure
- name: Agstack Openagri Farm Calendar Patchedalert Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-patchedalert-structure
- name: Agstack Openagri Farm Calendar Patchedcompostoperation Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-patchedcompostoperation-structure
- name: Agstack Openagri Farm Calendar Patchedcompostturningoperation Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-patchedcompostturningoperation-structure
- name: Agstack Openagri Farm Calendar Patchedcropgrowthstageobservation Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-patchedcropgrowthstageobservation-structure
- name: Agstack Openagri Farm Calendar Patchedcropprotectionoperation Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-patchedcropprotectionoperation-structure
- name: Agstack Openagri Farm Calendar Patchedcropstressindicatorobservation Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-patchedcropstressindicatorobservation-structure
- name: Agstack Openagri Farm Calendar Patcheddiseasedetectionobservation Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-patcheddiseasedetectionobservation-structure
- name: Agstack Openagri Farm Calendar Patchedfarm Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-patchedfarm-structure
- name: Agstack Openagri Farm Calendar Patchedfarmanimal Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-patchedfarmanimal-structure
- name: Agstack Openagri Farm Calendar Patchedfarmcalendaractivity Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-patchedfarmcalendaractivity-structure
- name: Agstack Openagri Farm Calendar Patchedfarmcalendaractivitytype Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-patchedfarmcalendaractivitytype-structure
- name: Agstack Openagri Farm Calendar Patchedfarmcrop Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-patchedfarmcrop-structure
- name: Agstack Openagri Farm Calendar Patchedfarmparcel Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-patchedfarmparcel-structure
- name: Agstack Openagri Farm Calendar Patchedfertilizationoperation Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-patchedfertilizationoperation-structure
- name: Agstack Openagri Farm Calendar Patchedfertilizer Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-patchedfertilizer-structure
- name: Agstack Openagri Farm Calendar Patchedgenericfarmasset Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-patchedgenericfarmasset-structure
- name: Agstack Openagri Farm Calendar Patchedirrigationoperation Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-patchedirrigationoperation-structure
- name: Agstack Openagri Farm Calendar Patchedobservation Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-patchedobservation-structure
- name: Agstack Openagri Farm Calendar Patchedpesticide Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-patchedpesticide-structure
- name: Agstack Openagri Farm Calendar Patchedsprayingrecommendationobservation Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-patchedsprayingrecommendationobservation-structure
- name: Agstack Openagri Farm Calendar Patchedvigorestimationobservation Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-patchedvigorestimationobservation-structure
- name: Agstack Openagri Farm Calendar Patchedyieldpredictionobservation Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-patchedyieldpredictionobservation-structure
- name: Agstack Openagri Farm Calendar Pesticide Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-pesticide-structure
- name: Agstack Openagri Farm Calendar Sprayingrecommendationobservation Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-sprayingrecommendationobservation-structure
- name: Agstack Openagri Farm Calendar Vigorestimationobservation Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-vigorestimationobservation-structure
- name: Agstack Openagri Farm Calendar Yieldpredictionobservation Structure
  property_count: 0
  slug: agstack-openagri-farm-calendar-yieldpredictionobservation-structure
- name: Agstack Openagri Weather Service Authtoken Structure
  property_count: 0
  slug: agstack-openagri-weather-service-authtoken-structure
- name: Agstack Openagri Weather Service Body Token Auth Token Post Structure
  property_count: 0
  slug: agstack-openagri-weather-service-body-token-auth-token-post-structure
- name: Agstack Openagri Weather Service Flightstatusforecastresponse Structure
  property_count: 0
  slug: agstack-openagri-weather-service-flightstatusforecastresponse-structure
- name: Agstack Openagri Weather Service Geojsonout Structure
  property_count: 0
  slug: agstack-openagri-weather-service-geojsonout-structure
- name: Agstack Openagri Weather Service Httpvalidationerror Structure
  property_count: 0
  slug: agstack-openagri-weather-service-httpvalidationerror-structure
- name: Agstack Openagri Weather Service Jsonldgraph Structure
  property_count: 0
  slug: agstack-openagri-weather-service-jsonldgraph-structure
- name: Agstack Openagri Weather Service Pointout Structure
  property_count: 0
  slug: agstack-openagri-weather-service-pointout-structure
- name: Agstack Openagri Weather Service Predictionout Structure
  property_count: 0
  slug: agstack-openagri-weather-service-predictionout-structure
- name: Agstack Openagri Weather Service Sprayforecastresponse Structure
  property_count: 0
  slug: agstack-openagri-weather-service-sprayforecastresponse-structure
- name: Agstack Openagri Weather Service Thidataout Structure
  property_count: 0
  slug: agstack-openagri-weather-service-thidataout-structure
- name: Agstack Openagri Weather Service Validationerror Structure
  property_count: 0
  slug: agstack-openagri-weather-service-validationerror-structure
- name: Agstack Openagri Weather Service Weatherdataout Structure
  property_count: 0
  slug: agstack-openagri-weather-service-weatherdataout-structure
jsonld:
- class_count: 30
  name: Agstack Context
  property_count: 6
  slug: agstack-context
layout: provider
modified: '2026-05-19'
name: AgStack Foundation
nav: Providers
network: true
overview: 'AgStack Foundation publishes 7 APIs on the [APIs.io](https://apis.io/) network, including api API, Auth API, Authentication API, and 4 more. Tagged areas include Agriculture, Linux Foundation, Open Source, Geospatial, and Precision Agriculture.


  The AgStack Foundation catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  AgStack Foundation''s developer surface includes authentication, engineering blog, developer portal, documentation, and 8 more developer resources.'
plans:
- name: Agstack Plans Pricing
  plan_count: 3
  slug: agstack-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 5
  name: Agstack Rate Limits
  slug: agstack-rate-limits
rules:
- name: AgStack Foundation API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: agstack-jsonschema-spectral-rules
- name: AgStack Foundation API Rules
  rule_count: 25
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 17
  slug: agstack-spectral-rules
score:
  band: developing
  composite: 49.5
  delta: -4.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 66.1
    developer_ergonomics: 30.4
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 53.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agstack/refs/heads/main/screenshots/agstack-2026-06-20T170504.png
security:
- kind: authentication
  name: Agstack Authentication
  slug: agstack-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Agstack Domain Security
  slug: agstack-domain-security
  summary_line: TLSv1.3 · HSTS
slug: agstack
tags:
- Agriculture
- Linux Foundation
- Open Source
- Geospatial
- Precision Agriculture
- Linked Data
use_cases:
- description: Farmers and agri-cooperatives register field boundaries in the global asset registry to enable data-driven farm management
  name: Farmer Field Registration
- description: Check spray conditions and UAV flight forecasts before applying pesticides or fertilizers to minimize drift and maximize efficacy
  name: Crop Protection Planning
- description: Monitor Temperature-Humidity Index to detect and prevent heat stress events in dairy and beef cattle herds
  name: Livestock Heat Stress Monitoring
- description: Register plot geolocations and trace agricultural commodities through the supply chain to demonstrate zero-deforestation compliance
  name: EUDR Supply Chain Compliance
- description: Use evapotranspiration data and soil moisture analysis to schedule irrigation and optimize water usage
  name: Precision Irrigation
- description: Share agricultural data between platforms using JSON-LD/OCSM linked data format for semantic interoperability
  name: Interoperable Agtech Integration
website: https://agstack.org/
---
