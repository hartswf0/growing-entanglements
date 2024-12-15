# Growing Entanglements

An interactive exploration of cultural theory through digital interfaces and network visualizations. This project examines the theoretical frameworks of Marshall Sahlins and Gananath Obeyesekere through various interactive interfaces and visualizations.

## Project Structure

- `index.html` - Main project documentation and interface analysis
- `Resistance-Topology-Visualization.html` - Interactive network visualization
- `info-arch-nav.html` - Information architecture navigator
- `reference.txt` - Bibliography and references
- `README-theory.md` - Theoretical background and documentation

## Features

1. **Spectral Negotiation Interface**
   - Explores theoretical intersections
   - Visualizes conceptual relationships

2. **Flux Field Visualization**
   - PIE-BDI Network ForceGraph implementation
   - Interactive network visualization of theoretical frameworks

3. **Information Architecture Navigator**
   - Dynamic navigation of theoretical concepts
   - Interactive relationship mapping

## Getting Started

1. Clone the repository
2. Open `index.html` in a web browser
3. Navigate through the different interfaces using the navigation menu

## Theory and Background

See `README-theory.md` for detailed information about the theoretical framework and methodology.

## License

This project is part of academic research. All rights reserved.

# Resistance Topology: Hostile Architecture Simulation

A dynamic visualization system for analyzing the interplay between hostile architecture, community resistance, and social estrangement, based on Robert Rosenberger's postphenomenological analysis of hostile architecture and urban design.

## Theoretical Foundation

### Postphenomenological Framework
Drawing from Rosenberger's work on hostile architecture and urban exclusion, this simulation explores three key forces:

1. **Architectural Isolation** (Red)
   - Exclusion: Direct prevention of rest/dwelling
   - Marginalization: Subtle design barriers
   - Spatial Violence: Aggressive environmental modifications

2. **Persistent Resistance** (Green)
   - Reclamation: Community reappropriation of space
   - Disruption: Direct action against hostile elements
   - Counter-design: Alternative inclusive proposals

3. **Estrangement Mechanism** (Gray)
   - Psychological Distancing: Social-spatial alienation
   - Normative Control: Behavioral modification
   - Subtle Oppression: Systemic exclusion

### Theoretical Concepts
- **Multistability**: How urban objects can embody multiple competing interpretations
- **Material Politics**: The role of design in enforcing social policies
- **Spatial Justice**: The right to occupy and use public space
- **Technological Mediation**: How architecture shapes social relations

## Technical Architecture

### Visualization System
- Force-directed graph using D3.js
- Dynamic node positioning representing force relationships
- Color-coded behavior amplification/attenuation
- Real-time topology analysis

### Core Components
1. **Entity System**
   ```javascript
   const entities = [
     { id: "isolation", color: "#8B0000" },
     { id: "resistance", color: "#004d00" },
     { id: "estrangement", color: "#4a4a4a" }
   ]
   ```

2. **Behavior Network**
   - Weighted relationships between forces
   - Dynamic score calculation based on spatial proximity
   - Influence propagation through network

3. **Narrative System**
The monitoring system tracks the evolution of forces and behaviors through:

1. **Real-time State Tracking**
   - Captures dominant and secondary force interactions
   - Records behavior intensities and relationships
   - Maintains temporal sequence of events

2. **Daily Reports**
   ```json
   {
     "simulation_id": "RT-1702342907123",
     "total_days": 5,
     "entries": [{
       "day": 1,
       "timestamp": "2024-12-11T20:07:23.000Z",
       "dominant": {
         "type": "resistance",
         "intensity": 0.85
       },
       "secondary": {
         "type": "isolation",
         "intensity": 0.32
       },
       "narrative": "Community Response: Counter-design initiatives gain momentum..."
     }]
   }
   ```

3. **Visual Feedback**
   - Color-coded entries matching force colors
   - Daily progression with clear timestamps
   - Impact metrics for dominant/secondary forces
   - Narrative descriptions of key events

### Data Structure
```json
{
  "simulation_id": "RT-[timestamp]",
  "entries": [{
    "day": 1,
    "dominant_force": "resistance",
    "actions": {
      "amplifying": {
        "type": "resistance",
        "action": "counter-design",
        "score": 0.85
      },
      "attenuating": {
        "type": "isolation",
        "action": "exclusion",
        "score": 0.32
      }
    }
  }]
}
```

## Usage

1. **Visualization Interaction**
   - Drag nodes to adjust force relationships
   - Observe behavior amplification/attenuation
   - Track narrative developments

2. **Analysis Tools**
   - Export simulation data as JSON
   - Monitor force dominance patterns
   - Track behavioral evolution

3. **Interpretation**
   - Identify emerging resistance patterns
   - Analyze effectiveness of counter-measures
   - Study spatial justice dynamics

## References

Rosenberger, R. (2020). "On Hostile Design: Theoretical and Empirical Prospects." Urban Studies.

Rosenberger, R. (2017). "Callous Objects: Designs against the Homeless." University of Minnesota Press.

## License
MIT License - Open for academic and research use
