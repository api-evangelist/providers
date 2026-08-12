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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 36
  human_in_the_loop: 2
  name: Sentinel Hub Agentic Access
  operation_count: 95
  slug: sentinel-hub-agentic-access
  summary_line: 95 operations · 36 acting · 2 human-in-the-loop
api_count: 26
apis:
- description: OGC-standard web services (WMS, WCS, WFS, WMTS) for integrating Sentinel Hub satellite imagery into GIS applications such as QGIS, ArcGIS, OpenLayers, and Google Earth. Authentication uses a configura
  name: Sentinel Hub OGC Services
  slug: ogc
- description: '**NOTE:** _Asynchronous Processing API is currently in beta release._'
  name: Sentinel Hub async_process API
  slug: sentinel-hub-async-process-api
- description: The batch_statistical API from Sentinel Hub — 6 operation(s) for batch_statistical.
  name: Sentinel Hub batch_statistical API
  slug: sentinel-hub-batch-statistical-api
- description: The batch_v2_process API from Sentinel Hub — 5 operation(s) for batch_v2_process.
  name: Sentinel Hub batch_v2_process API
  slug: sentinel-hub-batch-v2-process-api
- description: The batch_v2_tiling_grid API from Sentinel Hub — 2 operation(s) for batch_v2_tiling_grid.
  name: Sentinel Hub batch_v2_tiling_grid API
  slug: sentinel-hub-batch-v2-tiling-grid-api
- description: The byoc_collection API from Sentinel Hub — 3 operation(s) for byoc_collection.
  name: Sentinel Hub byoc_collection API
  slug: sentinel-hub-byoc-collection-api
- description: The byoc_tile API from Sentinel Hub — 5 operation(s) for byoc_tile.
  name: Sentinel Hub byoc_tile API
  slug: sentinel-hub-byoc-tile-api
- description: This is an OpenAPI definition of the SpatioTemporal Asset Catalog API - Collections specification. This is a subset of the STAC API - Features specification.
  name: Sentinel Hub catalog_collections API
  slug: sentinel-hub-catalog-collections-api
- description: This is an OpenAPI definition of the SpatioTemporal Asset Catalog API - Core specification. Any service that implements this endpoint to allow discovery of spatiotemporal assets can be considered a ST
  name: Sentinel Hub catalog_core API
  slug: sentinel-hub-catalog-core-api
- description: 'This is an OpenAPI definition of the SpatioTemporal Asset Catalog API - Features specification. This extends OGC API - Features - Part 1: Core.'
  name: Sentinel Hub catalog_features API
  slug: sentinel-hub-catalog-features-api
- description: This is an OpenAPI definition of the SpatioTemporal Asset Catalog API - Item Search specification.
  name: Sentinel Hub catalog_item_search API
  slug: sentinel-hub-catalog-item-search-api
- description: TPDI Service for Planet data is deprecated and will be sunset on November 11th, 2026. Please use [Planet Orders API](https://docs.planet.com/develop/apis/orders/reference/) instead.
  name: Sentinel Hub dataimport_delivery API
  slug: sentinel-hub-dataimport-delivery-api
- description: TPDI Service for Planet data is deprecated and will be sunset on November 11th, 2026. Please use [Planet Orders API](https://docs.planet.com/develop/apis/orders/reference/) instead.
  name: Sentinel Hub dataimport_order API
  slug: sentinel-hub-dataimport-order-api
- description: TPDI Service for Planet data is deprecated and will be sunset on November 11th, 2026. Please use [Planet Data API](https://docs.planet.com/develop/apis/data/reference/) instead.
  name: Sentinel Hub dataimport_product API
  slug: sentinel-hub-dataimport-product-api
- description: The dataimport_quota API from Sentinel Hub — 2 operation(s) for dataimport_quota.
  name: Sentinel Hub dataimport_quota API
  slug: sentinel-hub-dataimport-quota-api
- description: TPDI Service for Planet data is deprecated and will be sunset on November 11th, 2026. Please use [Planet Item Search](https://docs.planet.com/develop/apis/data/reference/#tag/Item-Search) instead.
  name: Sentinel Hub dataimport_search API
  slug: sentinel-hub-dataimport-search-api
- description: TPDI Service for Planet data is deprecated and will be sunset on November 11th, 2026. Please use [Planet Subscriptions API](https://docs.planet.com/develop/apis/subscriptions/reference/) instead.
  name: Sentinel Hub dataimport_subscription API
  slug: sentinel-hub-dataimport-subscription-api
- description: TPDI Service for Planet data is deprecated and will be sunset on November 11th, 2026. Please use [Planet Subscriptions API](https://docs.planet.com/develop/apis/subscriptions/reference/) instead.
  name: Sentinel Hub dataimport_subscription_delivery API
  slug: sentinel-hub-dataimport-subscription-delivery-api
- description: TPDI Service for Planet data is deprecated and will be sunset on November 11th, 2026. Please use the [BYOC API](https://docs.planet.com/develop/apis/byoc/reference/#tag/byoc_tile) instead to work with
  name: Sentinel Hub dataimport_subscription_tile_delivery API
  slug: sentinel-hub-dataimport-subscription-tile-delivery-api
- description: TPDI Service for Planet data is deprecated and will be sunset on November 11th, 2026. Please use the [BYOC API](https://docs.planet.com/develop/apis/byoc/reference/#tag/byoc_tile) instead to work with
  name: Sentinel Hub dataimport_tile_delivery API
  slug: sentinel-hub-dataimport-tile-delivery-api
- description: The metadata_collection API from Sentinel Hub — 3 operation(s) for metadata_collection.
  name: Sentinel Hub metadata_collection API
  slug: sentinel-hub-metadata-collection-api
- description: The metadata_location API from Sentinel Hub — 2 operation(s) for metadata_location.
  name: Sentinel Hub metadata_location API
  slug: sentinel-hub-metadata-location-api
- description: Make sure to use the appropriate <a href="https://docs.sentinel-hub.com/api/latest/data/" target="_blank">end-point for each of the datasets</a>, e.g. for Landsat, Sentinel-3, etc.
  name: Sentinel Hub process API
  slug: sentinel-hub-process-api
- description: The statistical API from Sentinel Hub — 1 operation(s) for statistical.
  name: Sentinel Hub statistical API
  slug: sentinel-hub-statistical-api
- description: The zarr_array API from Sentinel Hub — 2 operation(s) for zarr_array.
  name: Sentinel Hub zarr_array API
  slug: sentinel-hub-zarr-array-api
- description: The zarr_collection API from Sentinel Hub — 3 operation(s) for zarr_collection.
  name: Sentinel Hub zarr_collection API
  slug: sentinel-hub-zarr-collection-api
artifact_total: 317
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sentinel-hub-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sentinel-hub-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sentinel-hub-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sentinel-hub-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.sentinel-hub.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sentinel-hub.com/api/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sentinel-hub.com/api/latest/reference/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.sentinel-hub.com/api/latest/api/overview/authentication/
- group: commercial
  title: ''
  type: Billing
  url: https://docs.sentinel-hub.com/api/latest/api/overview/billing/
- group: operate
  title: ''
  type: RateLimiting
  url: https://docs.sentinel-hub.com/api/latest/api/overview/rate-limiting/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/sentinel-hub
- group: operate
  title: ''
  type: Forums
  url: https://forum.sentinel-hub.com/
- group: other
  title: ''
  type: Dashboard
  url: https://apps.sentinel-hub.com/dashboard/
- group: commercial
  title: ''
  type: Plans
  url: plans/sentinel-hub-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sentinel-hub-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sentinel-hub-finops.yml
created: '2026-06-13'
description: Sentinel Hub by Sinergise is a cloud-based satellite imagery processing platform providing REST APIs for accessing, processing, and analysing data from Sentinel, Landsat, MODIS, and commercial satellite constellations. APIs deliver raw imagery, rendered images, and geospatial statistics on demand using custom EvalScript processing without requiring data downloads.
examples:
- key_count: 6
  name: Getcatalogitemsearch  Resp 200  Response_200
  slug: getCatalogItemSearch--resp-200--response_200
- key_count: 5
  name: Postcatalogitemsearch  Default
  slug: postCatalogItemSearch--default
- key_count: 6
  name: Postcatalogitemsearch  Resp 200  Response_200
  slug: postCatalogItemSearch--resp-200--response_200
finops:
- name: Sentinel Hub Finops
  service_category: Geospatial and Earth Observation
  slug: sentinel-hub-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sentinel-hub.png
json_schemas:
- name: Aggregation
  property_count: 2
  slug: Aggregation
- name: AnalysisReadyPlanetScopeDataSpec
  property_count: 3
  slug: AnalysisReadyPlanetScopeDataSpec
- name: ArrayOverride
  property_count: 0
  slug: ArrayOverride
- name: ArrayOverrides
  property_count: 0
  slug: ArrayOverrides
- name: ArrayParameters
  property_count: 5
  slug: ArrayParameters
- name: AsyncProcessGSBucketInfoTemplated
  property_count: 2
  slug: AsyncProcessGSBucketInfoTemplated
- name: AsyncProcessOutputDelivery
  property_count: 1
  slug: AsyncProcessOutputDelivery
- name: AsyncProcessOutputDeliveryV2
  property_count: 0
  slug: AsyncProcessOutputDeliveryV2
- name: AsyncProcessRequest
  property_count: 4
  slug: AsyncProcessRequest
- name: AsyncProcessRequestOutput
  property_count: 6
  slug: AsyncProcessRequestOutput
- name: AsyncProcessS3BucketInfoTemplated
  property_count: 5
  slug: AsyncProcessS3BucketInfoTemplated
- name: AsyncStatusResponse
  property_count: 2
  slug: AsyncStatusResponse
- name: BYOCCollection
  property_count: 9
  slug: BYOCCollection
- name: BYOCCollectionAdditionalData
  property_count: 6
  slug: BYOCCollectionAdditionalData
- name: BYOCCollectionMetadata
  property_count: 5
  slug: BYOCCollectionMetadata
- name: BYOCCollectionResponse
  property_count: 1
  slug: BYOCCollectionResponse
- name: BYOCCollectionUpdatePayload
  property_count: 4
  slug: BYOCCollectionUpdatePayload
- name: BYOCCollectionsResponse
  property_count: 2
  slug: BYOCCollectionsResponse
- name: BYOC / BATCH / ZARR
  property_count: 0
  slug: BYOCDataset
- name: BYOCFiltering
  property_count: 2
  slug: BYOCFiltering
- name: BYOCFormat
  property_count: 6
  slug: BYOCFormat
- name: BYOCTile
  property_count: 8
  slug: BYOCTile
- name: BYOCTileAdditionalData
  property_count: 2
  slug: BYOCTileAdditionalData
- name: BYOCTileResponse
  property_count: 1
  slug: BYOCTileResponse
- name: BYOCTileStatus
  property_count: 0
  slug: BYOCTileStatus
- name: BYOCTileUpdatePayload
  property_count: 2
  slug: BYOCTileUpdatePayload
- name: BYOCTilesResponse
  property_count: 2
  slug: BYOCTilesResponse
- name: BandMetadata
  property_count: 2
  slug: BandMetadata
- name: BandStatistics
  property_count: 2
  slug: BandStatistics
- name: BaseDataset
  property_count: 2
  slug: BaseDataset
- name: BaseDatasetProcessing
  property_count: 2
  slug: BaseDatasetProcessing
- name: BatchCogParameters
  property_count: 6
  slug: BatchCogParameters
- name: BatchCollectionMetadata
  property_count: 5
  slug: BatchCollectionMetadata
- name: BatchProcessOutput
  property_count: 7
  slug: BatchProcessOutput
- name: BatchProcessRequest
  property_count: 19
  slug: BatchProcessRequest
- name: BatchStatisticalInput
  property_count: 2
  slug: BatchStatisticalInput
- name: BatchStatisticalRequest
  property_count: 4
  slug: BatchStatisticalRequest
- name: BatchStatisticalRequestAggregation
  property_count: 0
  slug: BatchStatisticalRequestAggregation
- name: BatchStatisticsTaskDto
  property_count: 0
  slug: BatchStatisticsTaskDto
- name: BatchStatisticsTaskStatusDto
  property_count: 8
  slug: BatchStatisticsTaskStatusDto
- name: BatchTileOrigin
  property_count: 3
  slug: BatchTileOrigin
- name: BatchV2ArrayOverride
  property_count: 0
  slug: BatchV2ArrayOverride
- name: BatchV2CogParameters
  property_count: 6
  slug: BatchV2CogParameters
- name: GeoPackageFeatureDefaults
  property_count: 3
  slug: BatchV2GeoPackageFeatureDefaults
- name: GeoPackageInput
  property_count: 3
  slug: BatchV2GeoPackageInput
- name: BatchV2ProcessInput
  property_count: 0
  slug: BatchV2ProcessInput
- name: BatchV2ProcessOutput
  property_count: 0
  slug: BatchV2ProcessOutput
- name: BatchV2ProcessRequest
  property_count: 4
  slug: BatchV2ProcessRequest
- name: BatchV2ProcessRequestUpdatePayload
  property_count: 1
  slug: BatchV2ProcessRequestUpdatePayload
- name: BatchV2ProcessTask
  property_count: 14
  slug: BatchV2ProcessTask
- name: RasterOutput
  property_count: 8
  slug: BatchV2RasterOutput
- name: BatchV2TilingGridDescriptor
  property_count: 3
  slug: BatchV2TilingGridDescriptor
- name: BatchV2TilingGridDescriptorProperties
  property_count: 4
  slug: BatchV2TilingGridDescriptorProperties
- name: TilingGridInput
  property_count: 5
  slug: BatchV2TilingGridInput
- name: ZarrOutput
  property_count: 5
  slug: BatchV2ZarrOutput
- name: BatchV2ZarrOutputArrayOverrides
  property_count: 0
  slug: BatchV2ZarrOutputArrayOverrides
- name: BatchV2ZarrOutputArrayParameters
  property_count: 5
  slug: BatchV2ZarrOutputArrayParameters
- name: BatchV2ZarrOutputGroup
  property_count: 3
  slug: BatchV2ZarrOutputGroup
- name: BatchZarrParameters
  property_count: 4
  slug: BatchZarrParameters
- name: Boom
  property_count: 5
  slug: Boom
- name: CalculationDefinition
  property_count: 2
  slug: CalculationDefinition
- name: assets
  property_count: 0
  slug: CatalogAssets
- name: bbox
  property_count: 0
  slug: CatalogBbox
- name: catalog
  property_count: 7
  slug: CatalogCatalog
- name: collection
  property_count: 12
  slug: CatalogCollection
- name: collections
  property_count: 2
  slug: CatalogCollectionsCollections
- name: conformanceClasses
  property_count: 1
  slug: CatalogConformanceClasses
- name: CatalogCoreLandingPage
  property_count: 0
  slug: CatalogCoreLandingPage
- name: datetime
  property_count: 0
  slug: CatalogDatetime
- name: exception
  property_count: 2
  slug: CatalogException
- name: extent
  property_count: 2
  slug: CatalogExtent
- name: featureCollectionGeoJSON
  property_count: 2
  slug: CatalogFeatureCollectionGeoJSON
- name: featureGeoJSON
  property_count: 3
  slug: CatalogFeatureGeoJSON
- name: featureCollectionGeoJSON
  property_count: 0
  slug: CatalogFeaturesFeatureCollectionGeoJSON
- name: numberReturned
  property_count: 0
  slug: CatalogFeaturesNumberReturned
- name: timeStamp
  property_count: 0
  slug: CatalogFeaturesTimeStamp
- name: geometryGeoJSON
  property_count: 0
  slug: CatalogGeometryGeoJSON
- name: geometrycollectionGeoJSON
  property_count: 2
  slug: CatalogGeometrycollectionGeoJSON
- name: item
  property_count: 9
  slug: CatalogItem
- name: itemId
  property_count: 0
  slug: CatalogItemId
- name: bboxFilter
  property_count: 1
  slug: CatalogItemSearchBboxFilter
- name: collectionsArray
  property_count: 0
  slug: CatalogItemSearchCollectionsArray
- name: collectionsFilter
  property_count: 1
  slug: CatalogItemSearchCollectionsFilter
- name: itemCollection
  property_count: 1
  slug: CatalogItemSearchContextItemCollection
- name: datetimeFilter
  property_count: 1
  slug: CatalogItemSearchDatetimeFilter
- name: datetimeInterval
  property_count: 0
  slug: CatalogItemSearchDatetimeInterval
- name: distinct
  property_count: 0
  slug: CatalogItemSearchDistinctDistinct
- name: searchBody
  property_count: 1
  slug: CatalogItemSearchDistinctSearchBody
- name: fields
  property_count: 2
  slug: CatalogItemSearchFieldsFields
- name: searchBody
  property_count: 1
  slug: CatalogItemSearchFieldsSearchBody
- name: filter-cql2-json
  property_count: 0
  slug: CatalogItemSearchFilterFilterCql2Json
- name: filter-cql2-text
  property_count: 0
  slug: CatalogItemSearchFilterFilterCql2Text
- name: filter-crs
  property_count: 0
  slug: CatalogItemSearchFilterFilterCrs
- name: filter-lang
  property_count: 0
  slug: CatalogItemSearchFilterFilterLang
- name: searchBody
  property_count: 3
  slug: CatalogItemSearchFilterSearchBody
- name: ids
  property_count: 0
  slug: CatalogItemSearchIds
- name: idsFilter
  property_count: 1
  slug: CatalogItemSearchIdsFilter
- name: intersectsFilter
  property_count: 1
  slug: CatalogItemSearchIntersectsFilter
- name: itemCollection
  property_count: 3
  slug: CatalogItemSearchItemCollectionItemCollection
- name: limit
  property_count: 0
  slug: CatalogItemSearchLimit
- name: limitFilter
  property_count: 1
  slug: CatalogItemSearchLimitFilter
- name: searchBody
  property_count: 0
  slug: CatalogItemSearchSearchBody
- name: itemType
  property_count: 0
  slug: CatalogItemType
- name: license
  property_count: 0
  slug: CatalogLicense
- name: linestringGeoJSON
  property_count: 2
  slug: CatalogLinestringGeoJSON
- name: Link
  property_count: 8
  slug: CatalogLink
- name: links
  property_count: 0
  slug: CatalogLinks
- name: multilinestringGeoJSON
  property_count: 2
  slug: CatalogMultilinestringGeoJSON
- name: multipointGeoJSON
  property_count: 2
  slug: CatalogMultipointGeoJSON
- name: multipolygonGeoJSON
  property_count: 2
  slug: CatalogMultipolygonGeoJSON
- name: pointGeoJSON
  property_count: 2
  slug: CatalogPointGeoJSON
- name: polygonGeoJSON
  property_count: 2
  slug: CatalogPolygonGeoJSON
- name: properties
  property_count: 1
  slug: CatalogProperties
- name: providers
  property_count: 0
  slug: CatalogProviders
- name: STAC extensions
  property_count: 0
  slug: CatalogStacExtensions
- name: STAC version
  property_count: 0
  slug: CatalogStacVersion
- name: andExpression
  property_count: 2
  slug: Cql2AndExpression
- name: binaryComparisonPredicate
  property_count: 2
  slug: Cql2BinaryComparisonPredicate
- name: booleanExpression
  property_count: 0
  slug: Cql2BooleanExpression
- name: characterExpression
  property_count: 0
  slug: Cql2CharacterExpression
- name: comparisonPredicate
  property_count: 0
  slug: Cql2ComparisonPredicate
- name: isBetweenOperands
  property_count: 0
  slug: Cql2IsBetweenOperands
- name: isBetweenPredicate
  property_count: 2
  slug: Cql2IsBetweenPredicate
- name: cql2NotExpression
  property_count: 2
  slug: Cql2NotExpression
- name: numericExpression
  property_count: 0
  slug: Cql2NumericExpression
- name: propertyRef
  property_count: 1
  slug: Cql2PropertyRef
- name: scalarExpression
  property_count: 0
  slug: Cql2ScalarExpression
- name: scalarOperands
  property_count: 0
  slug: Cql2ScalarOperands
- name: CustomDatasetType
  property_count: 0
  slug: CustomDatasetType
- name: dem
  property_count: 0
  slug: DEMDataset
- name: DEMFiltering
  property_count: 1
  slug: DEMFiltering
- name: DEMProcessing
  property_count: 0
  slug: DEMProcessing
- name: DatasetType
  property_count: 0
  slug: DatasetType
- name: DateTimeInterval
  property_count: 2
  slug: DateTimeInterval
- name: DeliveryArchive
  property_count: 5
  slug: DeliveryArchive
- name: DeliveryArchiveFormat
  property_count: 0
  slug: DeliveryArchiveFormat
- name: DeliveryArchiveStatus
  property_count: 0
  slug: DeliveryArchiveStatus
- name: DeliveryStatus
  property_count: 0
  slug: DeliveryStatus
- name: DeliveryTile
  property_count: 3
  slug: DeliveryTile
- name: GSBucketInfo
  property_count: 2
  slug: GSBucketInfo
- name: GSBucketInfoTemplated
  property_count: 2
  slug: GSBucketInfoTemplated
- name: Geometry
  property_count: 0
  slug: Geometry
- name: Group
  property_count: 3
  slug: Group
- name: hls
  property_count: 0
  slug: HLSDataset
- name: HLSFiltering
  property_count: 4
  slug: HLSFiltering
- name: HistogramDefinition
  property_count: 5
  slug: HistogramDefinition
- name: Interpolator
  property_count: 0
  slug: Interpolator
- name: landsat-ot-l1
  property_count: 0
  slug: L8L1Dataset
- name: landsat-ot-l2
  property_count: 0
  slug: L8L2Dataset
- name: landsat-etm-l1
  property_count: 0
  slug: LETML1Dataset
- name: landsat-etm-l2
  property_count: 0
  slug: LETML2Dataset
- name: landsat-mss-l1
  property_count: 0
  slug: LMSSL1Dataset
- name: landsat-tm-l1
  property_count: 0
  slug: LTML1Dataset
- name: landsat-tm-l2
  property_count: 0
  slug: LTML2Dataset
- name: LandsatDataset
  property_count: 0
  slug: LandsatDataset
- name: LandsatFiltering
  property_count: 3
  slug: LandsatFiltering
- name: LandsatTierFilteringWithRt
  property_count: 1
  slug: LandsatTierFilteringWithRt
- name: LandsatTierFilteringWithoutRt
  property_count: 1
  slug: LandsatTierFilteringWithoutRt
- name: Location
  property_count: 6
  slug: Location
- name: landsat-8-l1c
  property_count: 0
  slug: Ls8Dataset
- name: MaxCloudCoverage
  property_count: 0
  slug: MaxCloudCoverage
- name: MaxarDeliveryProvider
  property_count: 1
  slug: MaxarDeliveryProvider
- name: MaxarMaxOffNadir
  property_count: 0
  slug: MaxarMaxOffNadir
- name: MaxarMaxSunElevation
  property_count: 0
  slug: MaxarMaxSunElevation
- name: MaxarMinOffNadir
  property_count: 0
  slug: MaxarMinOffNadir
- name: MaxarMinSunElevation
  property_count: 0
  slug: MaxarMinSunElevation
- name: MaxarNativeSearchQuery
  property_count: 0
  slug: MaxarNativeSearchQuery
- name: MaxarOrderRequest
  property_count: 0
  slug: MaxarOrderRequest
- name: MaxarRequestBase
  property_count: 1
  slug: MaxarRequestBase
- name: MaxarSearchQuery
  property_count: 0
  slug: MaxarSearchQuery
- name: MaxarSearchResults
  property_count: 1
  slug: MaxarSearchResults
- name: MaxarSensor
  property_count: 0
  slug: MaxarSensor
- name: modis
  property_count: 0
  slug: ModisDataset
- name: ModisFiltering
  property_count: 2
  slug: ModisFiltering
- name: MultiPartBatchRequest
  property_count: 2
  slug: MultiPartBatchRequest
- name: MultiPartBatchV2Request
  property_count: 2
  slug: MultiPartBatchV2Request
- name: MultiPartProcessRequest
  property_count: 2
  slug: MultiPartProcessRequest
- name: MultiPartStatisticalRequest
  property_count: 2
  slug: MultiPartStatisticalRequest
- name: MultiPolygon
  property_count: 2
  slug: MultiPolygon
- name: NativeSearchQuery
  property_count: 0
  slug: NativeSearchQuery
- name: ObjectStorageInfo
  property_count: 1
  slug: ObjectStorageInfo
- name: ObjectStorageInfoV2
  property_count: 0
  slug: ObjectStorageInfoV2
- name: ObjectStorageOutputInfo
  property_count: 1
  slug: ObjectStorageOutputInfo
- name: ObjectStorageOutputInfoV2
  property_count: 0
  slug: ObjectStorageOutputInfoV2
- name: Order
  property_count: 7
  slug: Order
- name: OrderDelivery
  property_count: 0
  slug: OrderDelivery
- name: OrderDeliveryBase
  property_count: 4
  slug: OrderDeliveryBase
- name: OrderMaxarDelivery
  property_count: 0
  slug: OrderMaxarDelivery
- name: OrderPlanetDelivery
  property_count: 0
  slug: OrderPlanetDelivery
- name: OrderRequest
  property_count: 0
  slug: OrderRequest
- name: OrderStatus
  property_count: 0
  slug: OrderStatus
- name: PSSceneDataSpec
  property_count: 5
  slug: PSSceneDataSpec
- name: PlanetDeliveryProvider
  property_count: 1
  slug: PlanetDeliveryProvider
- name: PlanetNativeSearchQuery
  property_count: 0
  slug: PlanetNativeSearchQuery
- name: PlanetOrderRequest
  property_count: 0
  slug: PlanetOrderRequest
- name: PlanetOrderRequestBase
  property_count: 2
  slug: PlanetOrderRequestBase
- name: PlanetSearchQuery
  property_count: 0
  slug: PlanetSearchQuery
- name: PlanetSearchRequestBase
  property_count: 2
  slug: PlanetSearchRequestBase
- name: PlanetSearchResults
  property_count: 0
  slug: PlanetSearchResults
- name: PlanetSubscriptionDataFilterBase
  property_count: 1
  slug: PlanetSubscriptionDataFilterBase
- name: PlanetSubscriptionDataSpec
  property_count: 0
  slug: PlanetSubscriptionDataSpec
- name: PlanetSubscriptionRequest
  property_count: 0
  slug: PlanetSubscriptionRequest
- name: PlanetaryVariableDataSpec
  property_count: 3
  slug: PlanetaryVariableDataSpec
- name: Polygon
  property_count: 2
  slug: Polygon
- name: ProcessRequest
  property_count: 3
  slug: ProcessRequest
- name: ProcessRequestForBatch
  property_count: 3
  slug: ProcessRequestForBatch
- name: ProcessRequestForBatchV2
  property_count: 3
  slug: ProcessRequestForBatchV2
- name: Input
  property_count: 2
  slug: ProcessRequestInput
- name: Bounds
  property_count: 3
  slug: ProcessRequestInputBounds
- name: Bounds
  property_count: 3
  slug: ProcessRequestInputBoundsForBatchV2
- name: BoundsProperties
  property_count: 1
  slug: ProcessRequestInputBoundsProperties
- name: ProcessRequestInputData
  property_count: 0
  slug: ProcessRequestInputData
- name: Input
  property_count: 2
  slug: ProcessRequestInputForBatchV2
- name: ProcessRequestOutput
  property_count: 5
  slug: ProcessRequestOutput
- name: ProcessRequestOutputBatchResponse
  property_count: 2
  slug: ProcessRequestOutputBatchResponse
- name: ProcessRequestOutputBatchV2Response
  property_count: 2
  slug: ProcessRequestOutputBatchV2Response
- name: ProcessRequestOutputForBatch
  property_count: 1
  slug: ProcessRequestOutputForBatch
- name: ProcessRequestOutputForBatchV2
  property_count: 1
  slug: ProcessRequestOutputForBatchV2
- name: ProcessRequestOutputFormat
  property_count: 1
  slug: ProcessRequestOutputFormat
- name: image/jpeg
  property_count: 0
  slug: ProcessRequestOutputFormatJpeg
- name: application/json
  property_count: 0
  slug: ProcessRequestOutputFormatJson
- name: image/png
  property_count: 0
  slug: ProcessRequestOutputFormatPng
- name: image/tiff
  property_count: 0
  slug: ProcessRequestOutputFormatTiff
- name: zarr/array
  property_count: 0
  slug: ProcessRequestOutputFormatZarr
- name: ProcessRequestOutputResponse
  property_count: 2
  slug: ProcessRequestOutputResponse
- name: Quota
  property_count: 3
  slug: Quota
- name: QuotaExceededError
  property_count: 0
  slug: QuotaExceededError
- name: QuotaTpdiCollectionId
  property_count: 0
  slug: QuotaTpdiCollectionId
- name: ResourceReference
  property_count: 1
  slug: ResourceReference
- name: RestErrorWrapper
  property_count: 1
  slug: RestErrorWrapper
- name: sentinel-1-grd
  property_count: 0
  slug: S1Dataset
- name: S1Filtering
  property_count: 7
  slug: S1Filtering
- name: S1Processing
  property_count: 0
  slug: S1Processing
- name: S1ProcessingSpeckleFilterLEE
  property_count: 3
  slug: S1ProcessingSpeckleFilterLEE
- name: S1ProcessingSpeckleFilterNONE
  property_count: 1
  slug: S1ProcessingSpeckleFilterNONE
- name: sentinel-2-l1c
  property_count: 0
  slug: S2L1CDataset
- name: S2L1CFiltering
  property_count: 0
  slug: S2L1CFiltering
- name: sentinel-2-l2a
  property_count: 0
  slug: S2L2ADataset
- name: S2L2AFiltering
  property_count: 3
  slug: S2L2AFiltering
- name: S2Processing
  property_count: 0
  slug: S2Processing
- name: S3BucketInfo
  property_count: 5
  slug: S3BucketInfo
- name: S3BucketInfoTemplated
  property_count: 5
  slug: S3BucketInfoTemplated
- name: S3SlstrProcessing
  property_count: 0
  slug: S3SlstrProcessing
- name: S5PProcessing
  property_count: 0
  slug: S5PProcessing
- name: SearchQuery
  property_count: 0
  slug: SearchQuery
- name: SearchQueryBase
  property_count: 3
  slug: SearchQueryBase
- name: SearchResultBase
  property_count: 1
  slug: SearchResultBase
- name: SearchResults
  property_count: 0
  slug: SearchResults
- name: StatisticalDateTimeInterval
  property_count: 2
  slug: StatisticalDateTimeInterval
- name: StatisticalRequest
  property_count: 3
  slug: StatisticalRequest
- name: StatisticalRequestAggregation
  property_count: 0
  slug: StatisticalRequestAggregation
- name: StatisticalRequestAggregationWithoutEvalscript
  property_count: 6
  slug: StatisticalRequestAggregationWithoutEvalscript
- name: StatisticalRequestCalculations
  property_count: 0
  slug: StatisticalRequestCalculations
- name: StatisticalResponse
  property_count: 3
  slug: StatisticalResponse
- name: StatisticsDefinition
  property_count: 1
  slug: StatisticsDefinition
- name: Subscription
  property_count: 7
  slug: Subscription
- name: SubscriptionDelivery
  property_count: 0
  slug: SubscriptionDelivery
- name: SubscriptionDeliveryBase
  property_count: 3
  slug: SubscriptionDeliveryBase
- name: SubscriptionPlanetDelivery
  property_count: 0
  slug: SubscriptionPlanetDelivery
- name: SubscriptionRequest
  property_count: 0
  slug: SubscriptionRequest
- name: SubscriptionStatus
  property_count: 0
  slug: SubscriptionStatus
- name: TileStatus
  property_count: 0
  slug: TileStatus
- name: TilingGridDescriptor
  property_count: 3
  slug: TilingGridDescriptor
- name: TilingGridDescriptorProperties
  property_count: 4
  slug: TilingGridDescriptorProperties
- name: TilingGridSettings
  property_count: 4
  slug: TilingGridSettings
- name: TimeRange
  property_count: 2
  slug: TimeRange
- name: View
  property_count: 6
  slug: View
- name: ZArray
  property_count: 0
  slug: ZArray
- name: ZAttrs
  property_count: 0
  slug: ZAttrs
- name: ZarrArray
  property_count: 5
  slug: ZarrArray
- name: ZarrCollection
  property_count: 14
  slug: ZarrCollection
- name: ZarrCollectionAdditionalData
  property_count: 2
  slug: ZarrCollectionAdditionalData
- name: ZarrCollectionMetadata
  property_count: 5
  slug: ZarrCollectionMetadata
- name: ZarrCollectionUpdatePayload
  property_count: 1
  slug: ZarrCollectionUpdatePayload
- name: ZarrGetSingleArrayResponse
  property_count: 1
  slug: ZarrGetSingleArrayResponse
- name: ZarrQueryArraysResponse
  property_count: 1
  slug: ZarrQueryArraysResponse
- name: ZarrQueryCollectionsResponse
  property_count: 1
  slug: ZarrQueryCollectionsResponse
- name: ZarrSingleResponse
  property_count: 1
  slug: ZarrSingleResponse
jsonld:
- class_count: 0
  name: Sentinel Hub Api Context
  property_count: 0
  slug: sentinel-hub-api
- class_count: 278
  name: Sentinel Hub Context
  property_count: 0
  slug: sentinel-hub-context
layout: provider
modified: '2026-06-13'
name: Sentinel Hub
nav: Providers
network: true
overview: 'Sentinel Hub publishes 25 APIs on the [APIs.io](https://apis.io/) network, including async_process API, batch_statistical API, batch_v2_process API, and 22 more. Tagged areas include Satellite Imagery, Geospatial, Remote Sensing, Earth Observation, and NDVI.


  The Sentinel Hub catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Sentinel Hub''s developer surface includes authentication, documentation, API reference, GitHub presence, and 12 more developer resources.'
plans:
- name: Sentinel Hub Plans Pricing
  plan_count: 2
  slug: sentinel-hub-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 4
  name: Sentinel Hub Rate Limits
  slug: sentinel-hub-rate-limits
rules:
- name: Sentinel Hub API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sentinel-hub-jsonschema-spectral-rules
scopes:
- name: Sentinel Hub Scopes
  scope_count: 1
  slug: sentinel-hub-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 47.6
  delta: 0.3
  facets:
    commercial_clarity: 28.9
    contract_quality: 66.0
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 47.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 25
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sentinel-hub/refs/heads/main/screenshots/sentinel-hub-2026-06-20T193707.png
security:
- kind: authentication
  name: Sentinel Hub Authentication
  slug: sentinel-hub-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Sentinel Hub Domain Security
  slug: sentinel-hub-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sentinel-hub
tags:
- Satellite Imagery
- Geospatial
- Remote Sensing
- Earth Observation
- NDVI
- Sentinel
- Landsat
- MODIS
- OGC
- STAC
website: https://www.sentinel-hub.com/
---
