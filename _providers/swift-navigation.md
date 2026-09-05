---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.1
  scored_at: '2026-09-04'
api_count: 4
apis:
- description: Real-time GNSS corrections delivered as continuously-open NTRIP streams. A client opens an HTTP GET against a regional caster mountpoint with HTTP Basic credentials issued per device, and the caster w
  name: Skylark Precise Positioning Service
  slug: skylark-precise-positioning-service
- description: The native binary protocol for Swift Navigation devices — Piksi and Duro GNSS receivers and the Starling positioning engine. 242 message types across 29 packages carry position, velocity, baseline and
  name: Swift Binary Protocol (SBP)
  slug: swift-binary-protocol-sbp
- description: 'gRPC service for collecting, storing and analysing device location time series. DeviceService (5 RPCs) takes device state and events from the field; AppService (29 RPCs) queries and streams that data '
  name: Sora API
  slug: sora-api
- description: First-party, keyless JSON endpoints on the Swift Navigation website that power the Skylark User Portal and the receiver compatibility checker — the 134-entry third-party receiver compatibility catalog
  name: Swift Navigation Web Data Endpoints
  slug: swift-navigation-web-data-endpoints
artifact_total: 234
asyncapis:
- description: ''
  name: Swift Navigation Skylark Ntrip Streams
  slug: swift-navigation-skylark-ntrip-streams
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/swift-nav/libsbp/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swift-navigation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.swiftnav.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.swiftnav.com/support/solutions
- group: docs
  title: ''
  type: APIReference
  url: https://swift-nav.github.io/libsbp/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.swiftnav.com/get-started
- group: operate
  title: ''
  type: Support
  url: https://support.swiftnav.com/support/home
- group: company
  title: ''
  type: Blog
  url: https://www.swiftnav.com/resource-library
- group: company
  title: ''
  type: BlogRSS
  url: https://www.swiftnav.com/feed
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/swift-nav
- group: start
  title: ''
  type: SignUp
  url: https://account.swiftnav.com/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.swiftnav.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.swiftnav.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: conformance/swift-navigation-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/swift-navigation-conformance.yml
- group: build
  title: ''
  type: SDKs
  url: packages/swift-navigation-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/swift-navigation-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/swift-navigation-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/swift-navigation-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/swift-navigation-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/swift-navigation-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/swift-navigation-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/swift-navigation-changelog.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/swift-navigation-vocabulary.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/swift-navigation-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/swift-navigation-examples.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/swift-navigation-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/swift-navigation-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/swift-navigation-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/swift-navigation-scopes.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/swift-navigation-sora-api.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/swift-navigation-json-schema.yml
- group: docs
  title: ''
  type: Specification
  url: spec/swift-navigation-sbp-spec.yml
created: '2026-08-29'
description: Swift Navigation builds precise positioning technology for mass-market applications — automotive ADAS and autonomy, mobile handsets, robotics, drones, micromobility, fleet and asset tracking, GIS and construction. Its flagship service, Skylark, is a cloud-based GNSS corrections service that streams RTCM 3.x corrections over NTRIP from regional casters in North America, Europe and Asia Pacific, correcting satellite clock, orbit and atmospheric errors to take positioning from several metres to a few centimetres. Skylark ships in three variants — Nx RTK (network RTK on virtual reference stations), Cx (PPP-RTK, continent-wide, ISO 26262:2018 certified by UL Solutions) and Dx (differential code corrections for handsets and IoT). Swift also publishes the Swift Binary Protocol (SBP), the open, machine-readable wire protocol for its Piksi and Duro GNSS receivers and its Starling positioning engine, along with generated client libraries in six languages, and it publishes the complete
  gRPC contract for its Sora location time-series service on the Buf Schema Registry.
examples:
- key_count: 3
  name: Swift Navigation Skylark Receiver Catalog
  slug: swift-navigation-skylark-receiver-catalog
image: https://www.swiftnav.com/wp-content/uploads/SwiftNav-Social-Card.png
json_schemas:
- name: AcqSvProfile
  property_count: 12
  slug: AcqSvProfile
- name: AlmanacCommonContent
  property_count: 6
  slug: AlmanacCommonContent
- name: BoundsHeader
  property_count: 5
  slug: BoundsHeader
- name: CarrierPhase
  property_count: 2
  slug: CarrierPhase
- name: CodeBiasesContent
  property_count: 2
  slug: CodeBiasesContent
- name: CodePhaseBiasesSatSig
  property_count: 6
  slug: CodePhaseBiasesSatSig
- name: Doppler
  property_count: 2
  slug: Doppler
- name: ECDSASignature
  property_count: 2
  slug: ECDSASignature
- name: EphemerisCommonContent
  property_count: 6
  slug: EphemerisCommonContent
- name: EstimatedHorizontalErrorEllipse
  property_count: 3
  slug: EstimatedHorizontalErrorEllipse
- name: GNSSInputType
  property_count: 1
  slug: GNSSInputType
- name: GnssCapb
  property_count: 15
  slug: GnssCapb
- name: GnssSignal
  property_count: 2
  slug: GnssSignal
- name: GpsTime
  property_count: 3
  slug: GpsTime
- name: GpsTimeSec
  property_count: 2
  slug: GpsTimeSec
- name: GridElement
  property_count: 3
  slug: GridElement
- name: GridElementNoStd
  property_count: 3
  slug: GridElementNoStd
- name: GriddedCorrectionHeader
  property_count: 8
  slug: GriddedCorrectionHeader
- name: IMUInputType
  property_count: 1
  slug: IMUInputType
- name: IntegritySSRHeader
  property_count: 7
  slug: IntegritySSRHeader
- name: Latency
  property_count: 4
  slug: Latency
- name: MeasurementState
  property_count: 2
  slug: MeasurementState
- name: MsgAcknowledge
  property_count: 6
  slug: MsgAcknowledge
- name: MsgAcqResult
  property_count: 4
  slug: MsgAcqResult
- name: MsgAcqSvProfile
  property_count: 1
  slug: MsgAcqSvProfile
- name: MsgAesCmacSignature
  property_count: 6
  slug: MsgAesCmacSignature
- name: MsgAgeCorrections
  property_count: 2
  slug: MsgAgeCorrections
- name: MsgAlmanac
  property_count: 0
  slug: MsgAlmanac
- name: MsgAlmanacGPS
  property_count: 10
  slug: MsgAlmanacGPS
- name: MsgAlmanacGlo
  property_count: 8
  slug: MsgAlmanacGlo
- name: MsgAngularRate
  property_count: 5
  slug: MsgAngularRate
- name: MsgBasePosECEF
  property_count: 3
  slug: MsgBasePosECEF
- name: MsgBasePosLLH
  property_count: 3
  slug: MsgBasePosLLH
- name: MsgBaselineECEF
  property_count: 7
  slug: MsgBaselineECEF
- name: MsgBaselineHeading
  property_count: 4
  slug: MsgBaselineHeading
- name: MsgBaselineNED
  property_count: 8
  slug: MsgBaselineNED
- name: MsgBootloaderHandshakeReq
  property_count: 0
  slug: MsgBootloaderHandshakeReq
- name: MsgBootloaderHandshakeResp
  property_count: 2
  slug: MsgBootloaderHandshakeResp
- name: MsgBootloaderJumpToApp
  property_count: 1
  slug: MsgBootloaderJumpToApp
- name: MsgCertificateChain
  property_count: 5
  slug: MsgCertificateChain
- name: MsgCommandOutput
  property_count: 2
  slug: MsgCommandOutput
- name: MsgCommandReq
  property_count: 2
  slug: MsgCommandReq
- name: MsgCommandResp
  property_count: 2
  slug: MsgCommandResp
- name: MsgCsacTelemetry
  property_count: 2
  slug: MsgCsacTelemetry
- name: MsgCsacTelemetryLabels
  property_count: 2
  slug: MsgCsacTelemetryLabels
- name: MsgCwResults
  property_count: 0
  slug: MsgCwResults
- name: MsgCwStart
  property_count: 0
  slug: MsgCwStart
- name: MsgDeviceMonitor
  property_count: 5
  slug: MsgDeviceMonitor
- name: MsgDgnssStatus
  property_count: 4
  slug: MsgDgnssStatus
- name: MsgDops
  property_count: 7
  slug: MsgDops
- name: MsgEcdsaCertificate
  property_count: 4
  slug: MsgEcdsaCertificate
- name: MsgEcdsaSignature
  property_count: 6
  slug: MsgEcdsaSignature
- name: MsgEphemerisBds
  property_count: 24
  slug: MsgEphemerisBds
- name: MsgEphemerisGPS
  property_count: 23
  slug: MsgEphemerisGPS
- name: MsgEphemerisGal
  property_count: 25
  slug: MsgEphemerisGal
- name: MsgEphemerisGlo
  property_count: 9
  slug: MsgEphemerisGlo
- name: MsgEphemerisQzss
  property_count: 23
  slug: MsgEphemerisQzss
- name: MsgEphemerisSbas
  property_count: 6
  slug: MsgEphemerisSbas
- name: MsgExtEvent
  property_count: 5
  slug: MsgExtEvent
- name: MsgFileioConfigReq
  property_count: 1
  slug: MsgFileioConfigReq
- name: MsgFileioConfigResp
  property_count: 4
  slug: MsgFileioConfigResp
- name: MsgFileioReadDirReq
  property_count: 3
  slug: MsgFileioReadDirReq
- name: MsgFileioReadDirResp
  property_count: 2
  slug: MsgFileioReadDirResp
- name: MsgFileioReadReq
  property_count: 4
  slug: MsgFileioReadReq
- name: MsgFileioReadResp
  property_count: 2
  slug: MsgFileioReadResp
- name: MsgFileioRemove
  property_count: 1
  slug: MsgFileioRemove
- name: MsgFileioWriteReq
  property_count: 4
  slug: MsgFileioWriteReq
- name: MsgFileioWriteResp
  property_count: 1
  slug: MsgFileioWriteResp
- name: MsgFlashDone
  property_count: 1
  slug: MsgFlashDone
- name: MsgFlashErase
  property_count: 2
  slug: MsgFlashErase
- name: MsgFlashProgram
  property_count: 4
  slug: MsgFlashProgram
- name: MsgFlashReadReq
  property_count: 3
  slug: MsgFlashReadReq
- name: MsgFlashReadResp
  property_count: 3
  slug: MsgFlashReadResp
- name: MsgFrontEndGain
  property_count: 2
  slug: MsgFrontEndGain
- name: MsgFwd
  property_count: 3
  slug: MsgFwd
- name: MsgGPSTime
  property_count: 4
  slug: MsgGPSTime
- name: MsgGPSTimeGnss
  property_count: 4
  slug: MsgGPSTimeGnss
- name: MsgGloBiases
  property_count: 5
  slug: MsgGloBiases
- name: MsgGnssCapb
  property_count: 2
  slug: MsgGnssCapb
- name: MsgGnssTimeOffset
  property_count: 4
  slug: MsgGnssTimeOffset
- name: MsgGroupDelay
  property_count: 6
  slug: MsgGroupDelay
- name: MsgGroupMeta
  property_count: 4
  slug: MsgGroupMeta
- name: MsgHeartbeat
  property_count: 1
  slug: MsgHeartbeat
- name: MsgIarState
  property_count: 1
  slug: MsgIarState
- name: MsgImuAux
  property_count: 3
  slug: MsgImuAux
- name: MsgImuComp
  property_count: 8
  slug: MsgImuComp
- name: MsgImuRaw
  property_count: 8
  slug: MsgImuRaw
- name: MsgInsStatus
  property_count: 1
  slug: MsgInsStatus
- name: MsgInsUpdates
  property_count: 7
  slug: MsgInsUpdates
- name: MsgIono
  property_count: 9
  slug: MsgIono
- name: MsgLinuxCpuState
  property_count: 7
  slug: MsgLinuxCpuState
- name: MsgLinuxMemState
  property_count: 7
  slug: MsgLinuxMemState
- name: MsgLinuxProcessFdCount
  property_count: 4
  slug: MsgLinuxProcessFdCount
- name: MsgLinuxProcessFdSummary
  property_count: 2
  slug: MsgLinuxProcessFdSummary
- name: MsgLinuxProcessSocketCounts
  property_count: 6
  slug: MsgLinuxProcessSocketCounts
- name: MsgLinuxProcessSocketQueues
  property_count: 8
  slug: MsgLinuxProcessSocketQueues
- name: MsgLinuxSocketUsage
  property_count: 4
  slug: MsgLinuxSocketUsage
- name: MsgLinuxSysState
  property_count: 8
  slug: MsgLinuxSysState
- name: MsgLog
  property_count: 2
  slug: MsgLog
- name: MsgM25FlashWriteStatus
  property_count: 1
  slug: MsgM25FlashWriteStatus
- name: MsgMagRaw
  property_count: 5
  slug: MsgMagRaw
- name: MsgMaskSatellite
  property_count: 2
  slug: MsgMaskSatellite
- name: MsgMeasurementPoint
  property_count: 9
  slug: MsgMeasurementPoint
- name: MsgMeasurementState
  property_count: 1
  slug: MsgMeasurementState
- name: MsgNapDeviceDnaReq
  property_count: 0
  slug: MsgNapDeviceDnaReq
- name: MsgNapDeviceDnaResp
  property_count: 1
  slug: MsgNapDeviceDnaResp
- name: MsgNdbEvent
  property_count: 8
  slug: MsgNdbEvent
- name: MsgNetworkBandwidthUsage
  property_count: 1
  slug: MsgNetworkBandwidthUsage
- name: MsgNetworkStateReq
  property_count: 0
  slug: MsgNetworkStateReq
- name: MsgNetworkStateResp
  property_count: 8
  slug: MsgNetworkStateResp
- name: MsgObs
  property_count: 2
  slug: MsgObs
- name: MsgOdometry
  property_count: 3
  slug: MsgOdometry
- name: MsgOrientEuler
  property_count: 8
  slug: MsgOrientEuler
- name: MsgOrientQuat
  property_count: 10
  slug: MsgOrientQuat
- name: MsgOrientQuatCov
  property_count: 12
  slug: MsgOrientQuatCov
- name: MsgOsr
  property_count: 2
  slug: MsgOsr
- name: MsgPosECEF
  property_count: 7
  slug: MsgPosECEF
- name: MsgPosECEFCov
  property_count: 12
  slug: MsgPosECEFCov
- name: MsgPosECEFCovGnss
  property_count: 12
  slug: MsgPosECEFCovGnss
- name: MsgPosECEFGnss
  property_count: 7
  slug: MsgPosECEFGnss
- name: MsgPosLLH
  property_count: 8
  slug: MsgPosLLH
- name: MsgPosLLHAcc
  property_count: 13
  slug: MsgPosLLHAcc
- name: MsgPosLLHCov
  property_count: 12
  slug: MsgPosLLHCov
- name: MsgPosLLHCovGnss
  property_count: 12
  slug: MsgPosLLHCovGnss
- name: MsgPosLLHGnss
  property_count: 8
  slug: MsgPosLLHGnss
- name: MsgPoseRelative
  property_count: 22
  slug: MsgPoseRelative
- name: MsgPpsTime
  property_count: 2
  slug: MsgPpsTime
- name: MsgProfilingQueueInfo
  property_count: 3
  slug: MsgProfilingQueueInfo
- name: MsgProfilingResourceCounter
  property_count: 3
  slug: MsgProfilingResourceCounter
- name: MsgProfilingSystemInfo
  property_count: 4
  slug: MsgProfilingSystemInfo
- name: MsgProfilingThreadInfo
  property_count: 6
  slug: MsgProfilingThreadInfo
- name: MsgProtectionLevel
  property_count: 21
  slug: MsgProtectionLevel
- name: MsgReferenceFrameParam
  property_count: 20
  slug: MsgReferenceFrameParam
- name: MsgReset
  property_count: 1
  slug: MsgReset
- name: MsgResetFilters
  property_count: 1
  slug: MsgResetFilters
- name: MsgSbasRaw
  property_count: 4
  slug: MsgSbasRaw
- name: MsgSensorAidEvent
  property_count: 8
  slug: MsgSensorAidEvent
- name: MsgSetTime
  property_count: 0
  slug: MsgSetTime
- name: MsgSettingsReadByIndexDone
  property_count: 0
  slug: MsgSettingsReadByIndexDone
- name: MsgSettingsReadByIndexReq
  property_count: 1
  slug: MsgSettingsReadByIndexReq
- name: MsgSettingsReadByIndexResp
  property_count: 2
  slug: MsgSettingsReadByIndexResp
- name: MsgSettingsReadReq
  property_count: 1
  slug: MsgSettingsReadReq
- name: MsgSettingsReadResp
  property_count: 1
  slug: MsgSettingsReadResp
- name: MsgSettingsRegister
  property_count: 1
  slug: MsgSettingsRegister
- name: MsgSettingsRegisterResp
  property_count: 2
  slug: MsgSettingsRegisterResp
- name: MsgSettingsSave
  property_count: 0
  slug: MsgSettingsSave
- name: MsgSettingsWrite
  property_count: 1
  slug: MsgSettingsWrite
- name: MsgSettingsWriteResp
  property_count: 2
  slug: MsgSettingsWriteResp
- name: MsgSolnMeta
  property_count: 7
  slug: MsgSolnMeta
- name: MsgSpecan
  property_count: 7
  slug: MsgSpecan
- name: MsgSsrCodeBiases
  property_count: 5
  slug: MsgSsrCodeBiases
- name: MsgSsrCodePhaseBiasesBounds
  property_count: 5
  slug: MsgSsrCodePhaseBiasesBounds
- name: MsgSsrFlagHighLevel
  property_count: 15
  slug: MsgSsrFlagHighLevel
- name: MsgSsrFlagIonoGridPointSatLos
  property_count: 4
  slug: MsgSsrFlagIonoGridPointSatLos
- name: MsgSsrFlagIonoGridPoints
  property_count: 3
  slug: MsgSsrFlagIonoGridPoints
- name: MsgSsrFlagIonoTileSatLos
  property_count: 3
  slug: MsgSsrFlagIonoTileSatLos
- name: MsgSsrFlagSatellites
  property_count: 8
  slug: MsgSsrFlagSatellites
- name: MsgSsrFlagTropoGridPoints
  property_count: 3
  slug: MsgSsrFlagTropoGridPoints
- name: MsgSsrGriddedCorrection
  property_count: 4
  slug: MsgSsrGriddedCorrection
- name: MsgSsrGriddedCorrectionBounds
  property_count: 13
  slug: MsgSsrGriddedCorrectionBounds
- name: MsgSsrOrbitClock
  property_count: 14
  slug: MsgSsrOrbitClock
- name: MsgSsrOrbitClockBounds
  property_count: 5
  slug: MsgSsrOrbitClockBounds
- name: MsgSsrOrbitClockBoundsDegradation
  property_count: 5
  slug: MsgSsrOrbitClockBoundsDegradation
- name: MsgSsrPhaseBiases
  property_count: 9
  slug: MsgSsrPhaseBiases
- name: MsgSsrSatelliteApc
  property_count: 5
  slug: MsgSsrSatelliteApc
- name: MsgSsrStecCorrection
  property_count: 6
  slug: MsgSsrStecCorrection
- name: MsgSsrTileDefinition
  property_count: 13
  slug: MsgSsrTileDefinition
- name: MsgStatusJournal
  property_count: 5
  slug: MsgStatusJournal
- name: MsgStatusReport
  property_count: 5
  slug: MsgStatusReport
- name: MsgStmFlashLockSector
  property_count: 1
  slug: MsgStmFlashLockSector
- name: MsgStmFlashUnlockSector
  property_count: 1
  slug: MsgStmFlashUnlockSector
- name: MsgStmUniqueIdReq
  property_count: 0
  slug: MsgStmUniqueIdReq
- name: MsgStmUniqueIdResp
  property_count: 1
  slug: MsgStmUniqueIdResp
- name: MsgSvAzEl
  property_count: 1
  slug: MsgSvAzEl
- name: MsgTelSv
  property_count: 5
  slug: MsgTelSv
- name: MsgThreadState
  property_count: 3
  slug: MsgThreadState
- name: MsgTrackingIq
  property_count: 3
  slug: MsgTrackingIq
- name: MsgTrackingState
  property_count: 1
  slug: MsgTrackingState
- name: MsgUartState
  property_count: 5
  slug: MsgUartState
- name: MsgUserData
  property_count: 1
  slug: MsgUserData
- name: MsgUtcLeapSecond
  property_count: 4
  slug: MsgUtcLeapSecond
- name: MsgUtcTime
  property_count: 9
  slug: MsgUtcTime
- name: MsgUtcTimeGnss
  property_count: 9
  slug: MsgUtcTimeGnss
- name: MsgVelBody
  property_count: 12
  slug: MsgVelBody
- name: MsgVelCog
  property_count: 8
  slug: MsgVelCog
- name: MsgVelECEF
  property_count: 7
  slug: MsgVelECEF
- name: MsgVelECEFCov
  property_count: 12
  slug: MsgVelECEFCov
- name: MsgVelECEFCovGnss
  property_count: 12
  slug: MsgVelECEFCovGnss
- name: MsgVelECEFGnss
  property_count: 7
  slug: MsgVelECEFGnss
- name: MsgVelNED
  property_count: 8
  slug: MsgVelNED
- name: MsgVelNEDCov
  property_count: 12
  slug: MsgVelNEDCov
- name: MsgVelNEDCovGnss
  property_count: 12
  slug: MsgVelNEDCovGnss
- name: MsgVelNEDGnss
  property_count: 8
  slug: MsgVelNEDGnss
- name: MsgWheeltick
  property_count: 4
  slug: MsgWheeltick
- name: NetworkUsage
  property_count: 5
  slug: NetworkUsage
- name: ObservationHeader
  property_count: 2
  slug: ObservationHeader
- name: OdoInputType
  property_count: 1
  slug: OdoInputType
- name: OrbitClockBound
  property_count: 9
  slug: OrbitClockBound
- name: OrbitClockBoundDegradation
  property_count: 8
  slug: OrbitClockBoundDegradation
- name: PackedObsContent
  property_count: 7
  slug: PackedObsContent
- name: PackedOsrContent
  property_count: 8
  slug: PackedOsrContent
- name: Period
  property_count: 4
  slug: Period
- name: PhaseBiasesContent
  property_count: 5
  slug: PhaseBiasesContent
- name: QueueInfo
  property_count: 6
  slug: QueueInfo
- name: ResourceBucket
  property_count: 9
  slug: ResourceBucket
- name: STECHeader
  property_count: 7
  slug: STECHeader
- name: STECResidual
  property_count: 3
  slug: STECResidual
- name: STECResidualNoStd
  property_count: 2
  slug: STECResidualNoStd
- name: STECSatElement
  property_count: 3
  slug: STECSatElement
- name: STECSatElementIntegrity
  property_count: 5
  slug: STECSatElementIntegrity
- name: SatelliteAPC
  property_count: 5
  slug: SatelliteAPC
- name: SolutionInputType
  property_count: 2
  slug: SolutionInputType
- name: StatusJournalItem
  property_count: 2
  slug: StatusJournalItem
- name: SubSystemReport
  property_count: 3
  slug: SubSystemReport
- name: SvAzEl
  property_count: 3
  slug: SvAzEl
- name: SvId
  property_count: 2
  slug: SvId
- name: TelemetrySV
  property_count: 9
  slug: TelemetrySV
- name: TrackingChannelCorrelation
  property_count: 2
  slug: TrackingChannelCorrelation
- name: TrackingChannelState
  property_count: 3
  slug: TrackingChannelState
- name: TroposphericDelayCorrection
  property_count: 3
  slug: TroposphericDelayCorrection
- name: TroposphericDelayCorrectionNoStd
  property_count: 2
  slug: TroposphericDelayCorrectionNoStd
- name: UARTChannel
  property_count: 6
  slug: UARTChannel
- name: UtcTime
  property_count: 7
  slug: UtcTime
layout: provider
modified: '2026-08-29'
name: Swift Navigation
nav: Providers
network: true
overview: 'Swift Navigation publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, GNSS, Precise Positioning, Location, and Corrections.


  The Swift Navigation catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Swift Navigation''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, CLI, and 27 more developer resources.'
plans:
- name: Swift Navigation Plans Pricing
  plan_count: 0
  slug: swift-navigation-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Swift Navigation Rate Limits
  slug: swift-navigation-rate-limits
scopes:
- name: Swift Navigation Scopes
  scope_count: 0
  slug: swift-navigation-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 24
    catalog_earned: 51.0
    catalog_earned_first_party: 5.0
    catalog_gap: 64.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 33.3
    contract_quality: 55.8
    developer_ergonomics: 49.4
    discoverability: 74.1
    governance: 33.3
    operational_transparency: 26.3
  previous_composite: 40.2
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/swift-navigation/refs/heads/main/screenshots/swift-navigation-2026-09-02T161356.png
security:
- kind: authentication
  name: Swift Navigation Authentication
  slug: swift-navigation-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Swift Navigation Domain Security
  slug: swift-navigation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: swift-navigation
tags:
- Company
- GNSS
- Precise Positioning
- Location
- Corrections
- RTK
- NTRIP
- RTCM
- Automotive
- Geospatial
- IoT
- Robotics
- Protocols
website: https://www.swiftnav.com/
---
