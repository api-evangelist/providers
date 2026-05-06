---
aid: aircon
url: https://raw.githubusercontent.com/api-evangelist/aircon/refs/heads/main/apis.yml
name: Aircon
tags:
  - Air Conditioning
  - HVAC
  - Climate Control
  - IoT
  - Smart Home
  - Thermostat
  - Building Automation
  - Energy Management
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
description: A curated index of APIs, data sources, and developer resources related to air conditioning, HVAC (Heating, Ventilation, and Air Conditioning), and climate control systems. This topic collection covers smart thermostat APIs, building automation protocols, IoT climate APIs, and environmental data APIs used in residential, commercial, and industrial HVAC applications.
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: aircon:nest-device-access
    name: Google Nest Device Access API
    tags:
      - Thermostat
      - Smart Home
      - HVAC
      - Google
      - Nest
    humanURL: https://developers.home.google.com/nest/device-access
    baseURL: https://smartdevicemanagement.googleapis.com/v1
    description: The Nest Device Access API (Google Smart Device Management API) provides programmatic control over Nest thermostats, cameras, and doorbells. Supports reading thermostat state, setting target temperatures, switching HVAC modes, and managing heating/cooling schedules.
    properties:
      - url: https://developers.home.google.com/nest/device-access
        type: Documentation
      - url: https://developers.home.google.com/nest/device-access/api
        type: APIReference
      - url: https://smartdevicemanagement.googleapis.com/v1/$discovery/rest
        type: Discovery
  - aid: aircon:ecobee
    name: Ecobee API
    tags:
      - Thermostat
      - Smart Home
      - HVAC
      - Energy Management
    humanURL: https://www.ecobee.com/home/developer/api/introduction/index.shtml
    baseURL: https://api.ecobee.com
    description: The Ecobee API provides access to ecobee smart thermostats for reading and writing thermostat data, managing schedules, reading sensor data, and implementing custom home automation. Supports OAuth2 authentication and provides access to thermostat runtime data, alerts, and equipment status.
    properties:
      - url: https://www.ecobee.com/home/developer/api/introduction/index.shtml
        type: Documentation
      - url: https://www.ecobee.com/home/developer/api/introduction/index.shtml
        type: APIReference
  - aid: aircon:resideo-honeywell
    name: Resideo (Honeywell Home) API
    tags:
      - Thermostat
      - Smart Home
      - HVAC
      - Honeywell
    humanURL: https://developer.resideo.com
    baseURL: https://api.honeywell.com
    description: The Resideo API (formerly Honeywell Home API) provides access to Honeywell and Resideo smart thermostats and home security systems. Supports reading and controlling thermostat setpoints, modes, schedules, and fan operation. Uses OAuth2 and API key authentication.
    properties:
      - url: https://developer.resideo.com
        type: Documentation
      - url: https://developer.resideo.com/docs
        type: APIReference
  - aid: aircon:sensibo
    name: Sensibo API
    tags:
      - Air Conditioning
      - Smart Home
      - IoT
      - Energy Management
    humanURL: https://sensibo.github.io
    baseURL: https://home.sensibo.com/api/v2
    description: The Sensibo API provides control over Sensibo Sky and Air devices that add smart functionality to existing mini-split and window AC units. Supports reading AC state, setting temperature and mode, scheduling, and accessing historical usage data.
    properties:
      - url: https://sensibo.github.io
        type: Documentation
      - url: https://sensibo.github.io
        type: APIReference
  - aid: aircon:openweathermap
    name: OpenWeatherMap API
    tags:
      - Weather
      - Climate
      - Environmental Data
      - IoT
    humanURL: https://openweathermap.org/api
    baseURL: https://api.openweathermap.org/data/2.5
    description: OpenWeatherMap provides weather data APIs used in HVAC automation to adapt cooling/heating based on outdoor conditions. Offers current weather, forecasts, historical data, and air quality data relevant to climate control decisions.
    properties:
      - url: https://openweathermap.org/api
        type: Documentation
      - url: https://openweathermap.org/current
        type: APIReference
  - aid: aircon:home-assistant
    name: Home Assistant REST API
    tags:
      - Smart Home
      - HVAC
      - IoT
      - Open Source
      - Automation
    humanURL: https://developers.home-assistant.io/docs/api/rest/
    baseURL: http://homeassistant.local:8123/api
    description: The Home Assistant REST API provides access to all home automation entities including climate/HVAC entities. Supports reading thermostat state, setting temperature, changing HVAC mode, and triggering automations for air conditioning control.
    properties:
      - url: https://developers.home-assistant.io/docs/api/rest/
        type: Documentation
      - url: https://developers.home-assistant.io/docs/api/rest/
        type: APIReference
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Features
    data:
      - name: Thermostat Control
        description: APIs for reading and setting thermostat temperature, mode, and schedule.
      - name: HVAC Mode Management
        description: Switch between heating, cooling, auto, and fan-only modes programmatically.
      - name: Schedule Automation
        description: Create and manage time-based HVAC schedules and programs.
      - name: Sensor Data Access
        description: Read temperature, humidity, and occupancy sensor data from smart thermostats.
      - name: Energy Monitoring
        description: Track HVAC runtime, energy consumption, and efficiency metrics.
      - name: Weather Integration
        description: Combine outdoor weather data with HVAC control for predictive conditioning.
      - name: Smart Home Integration
        description: Integrate HVAC control with broader smart home platforms (Google Home, Apple HomeKit, SmartThings).
  - type: UseCases
    data:
      - name: Smart Home Automation
        description: Automate AC/heating based on occupancy, time, and weather conditions.
      - name: Energy Optimization
        description: Reduce energy costs by dynamically adjusting HVAC based on occupancy and utility pricing.
      - name: Building Management
        description: Commercial HVAC monitoring and control across multiple zones and buildings.
      - name: Comfort Monitoring
        description: Track and maintain optimal temperature and humidity levels.
      - name: Remote Control
        description: Control air conditioning remotely via mobile apps and API integrations.
      - name: Predictive Conditioning
        description: Pre-cool or pre-heat based on weather forecasts and schedules.
  - type: Integrations
    data:
      - name: Google Home
        description: Integration with Google Home and Google Assistant for voice control.
      - name: Apple HomeKit
        description: Integration with Apple HomeKit for iOS smart home control.
      - name: Amazon Alexa
        description: Voice control via Amazon Alexa smart home skills.
      - name: Home Assistant
        description: Open-source home automation platform with broad HVAC device support.
      - name: IFTTT
        description: Automation via IFTTT applets for condition-based HVAC control.
      - name: SmartThings
        description: Samsung SmartThings integration for HVAC devices.
  - url: https://raw.githubusercontent.com/api-evangelist/aircon/refs/heads/main/vocabulary/aircon-vocabulary.yaml
    type: Vocabulary
    title: Aircon Vocabulary
---
