---
aid: agrio
url: https://raw.githubusercontent.com/api-evangelist/agrio/refs/heads/main/apis.yml
modified: '2026-04-19'
description: Agrio is a precision plant protection solution that helps growers and crop advisors forecast, identify, and treat plant diseases, pests, and nutrient deficiencies. With Agrio APIs, developers can access AI-powered plant disease diagnosis from images, crop advisory data, weather pattern analysis, pest and disease predictions, and satellite vegetation monitoring to build accurate crop advisory tools.
tags:
  - Agriculture
  - Plant Disease
  - Pest Detection
  - AI
  - Crop Advisory
apis:
  - aid: agrio:agrio
    name: Agrio Agriculture API
    description: The Agrio Agriculture API provides AI-powered plant disease and pest diagnosis from images, plus crop advisory data, credit balance management, and access to a catalog of supported crop types. The Image Diagnosis API analyzes plant photos to return ranked disease and pest identifications with confidence scores, common names, and scientific names.
    humanURL: https://agrio.app/Agriculture-API/
    baseURL: https://agrio-api-gateway-6it0wqn1.uc.gateway.dev
    tags:
      - Plant Disease
      - Pest Detection
      - AI
      - Image Recognition
      - Crop Advisory
    properties:
      - type: Documentation
        url: https://agrio.app/Agriculture-API/
      - type: OpenAPI
        url: openapi/agrio-openapi-original.yml
      - type: JSONSchema
        url: json-schema/agrio-diagnosis-schema.json
        title: Diagnosis Schema
      - type: JSONSchema
        url: json-schema/agrio-diagnosis-result-schema.json
        title: Diagnosis Result Schema
      - type: JSONSchema
        url: json-schema/agrio-crop-schema.json
        title: Crop Schema
      - type: JSONSchema
        url: json-schema/agrio-credit-balance-schema.json
        title: Credit Balance Schema
      - type: JSONStructure
        url: json-structure/agrio-diagnosis-structure.json
        title: Diagnosis Structure
      - type: JSONStructure
        url: json-structure/agrio-crop-structure.json
        title: Crop Structure
      - type: JSON-LD
        url: json-ld/agrio-context.jsonld
common:
  - type: Website
    url: https://agrio.app
  - type: Portal
    url: https://pro.agrio.app/image-diagnosis-api
  - type: Support
    url: mailto:info@saillog.co
  - type: SpectralRules
    url: rules/agrio-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/crop-protection.yaml
  - type: Vocabulary
    url: vocabulary/agrio-vocabulary.yaml
  - type: Features
    data:
      - name: AI Image Diagnosis
        description: Computer vision algorithms identify plant diseases, pests, and nutrient deficiencies from uploaded photos with confidence scores.
      - name: AgrioShield Pest Prediction
        description: Predictive algorithms forecast disease pressure before or between scouting events to enable proactive intervention.
      - name: Satellite Imagery Alerts
        description: Remote sensing AI detects vegetation issues from satellite data, enabling early detection before visible symptoms appear.
      - name: Ranked Diagnoses
        description: Returns multiple ranked diagnoses with confidence scores, common names, and scientific names for disambiguation.
      - name: Credit-Based Usage
        description: API usage is metered using a credit system; one credit is consumed per diagnosis request.
      - name: Supported Crop Catalog
        description: Discoverable catalog of supported crop types for building targeted diagnosis workflows.
  - type: UseCases
    data:
      - name: Crop Advisory Tool Integration
        description: Embed AI plant disease diagnosis into existing crop advisory and farm management applications.
      - name: In-Field Disease Identification
        description: Enable agronomists and farmers to photograph plant symptoms and receive immediate AI-powered diagnosis.
      - name: Early Warning Systems
        description: Use AgrioShield alerts to notify growers when disease or pest conditions become favorable before visible symptoms appear.
      - name: Precision Agriculture Platforms
        description: Integrate Agrio diagnosis into precision agriculture platforms for targeted treatment recommendations.
      - name: Research and Development
        description: Access Agrio plant disease data for agricultural research and development of new advisory models.
  - type: Integrations
    data:
      - name: Weather Data Systems
        description: Agrio APIs integrate weather pattern data to enhance pest and disease prediction models.
      - name: Satellite Imagery Providers
        description: Remote sensing data from satellite providers is used for vegetation monitoring and anomaly detection.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
