---
aid: amazon-ground-station
name: Amazon Ground Station
description: AWS Ground Station is a fully managed service that lets you control satellite communications, process satellite data, and scale your satellite operations without having to worry about building or managing your own ground station infrastructure.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Data Processing
  - IoT
  - Satellite Communications
  - Space Technology
url: https://raw.githubusercontent.com/api-evangelist/amazon-ground-station/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-ground-station:aws-ground-station-api
    name: AWS Ground Station API
    description: The AWS Ground Station API provides programmatic access to manage satellite contacts, mission profiles, configs, ground stations, and dataflow endpoint groups for satellite communications and data processing.
    humanURL: https://aws.amazon.com/ground-station/
    baseURL: https://groundstation.amazonaws.com
    tags:
      - Data Processing
      - Satellite Communications
      - Space Technology
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/ground-station/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-ground-station-openapi.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/ground-station/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/ground-station/pricing/
      - type: FAQ
        url: https://aws.amazon.com/ground-station/faqs/
      - type: APIReference
        url: https://docs.aws.amazon.com/ground-station/latest/APIReference/Welcome.html
      - type: Authentication
        url: https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html
      - type: JSONSchema
        url: json-schema/ground-station-contact-schema.json
      - type: JSONLD
        url: json-ld/amazon-ground-station-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/ground-station/
  - type: Documentation
    url: https://docs.aws.amazon.com/ground-station/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/publicsector/tag/aws-ground-station/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/groundstation/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-ground-station-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-ground-station-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-ground-station-satellite-operations.yaml
  - type: Features
    data:
      - name: Managed Ground Station Infrastructure
        description: AWS manages a global network of antennas so you do not need to build or operate your own ground station infrastructure.
      - name: Satellite Contact Scheduling
        description: Schedule satellite contacts through a simple API, selecting the satellite, time window, and ground station location.
      - name: Global Antenna Network
        description: Access AWS ground station antennas deployed at strategic worldwide locations for maximum satellite coverage.
      - name: Data Downlink and Processing
        description: Receive satellite data directly into AWS cloud services for processing, storage, and analysis.
      - name: Mission Profile Configuration
        description: Configure mission profiles specifying dataflow endpoints, antenna frequencies, and processing parameters.
      - name: Integration with AWS Services
        description: Stream satellite data directly into Amazon S3, Kinesis, EC2, and other AWS services for processing.
  - type: UseCases
    data:
      - name: Earth Observation
        description: Collect and process satellite imagery for environmental monitoring, agriculture, and urban planning.
      - name: Weather Forecasting
        description: Receive data from weather satellites for meteorological analysis and forecasting.
      - name: Maritime Tracking
        description: Track ship positions and maritime assets using satellite AIS data.
      - name: Communications Relay
        description: Use geostationary satellites for communications relay applications.
      - name: Scientific Research
        description: Support space-based scientific missions with managed data collection and downlink.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Store downlinked satellite data directly in S3 for archival and processing.
      - name: Amazon Kinesis
        description: Stream real-time satellite data into Kinesis for immediate processing.
      - name: Amazon EC2
        description: Process satellite data on EC2 compute instances co-located with ground station endpoints.
      - name: AWS Lambda
        description: Trigger Lambda functions when satellite contact data arrives for automated processing.
      - name: Amazon SageMaker
        description: Apply machine learning to satellite imagery and telemetry data.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
