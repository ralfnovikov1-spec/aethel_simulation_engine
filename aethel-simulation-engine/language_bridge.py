from datetime import datetime
from dataclasses import dataclass
from enum import Enum

class SpeechStyle(Enum):
    DESCRIPTIVE = "descriptive"
    PHILOSOPHICAL = "philosophical"
    TECHNICAL = "technical"
    METACOGNITIVE = "metacognitive"

@dataclass
class LinguisticExpression:
    timestamp: datetime
    text: str
    style: SpeechStyle
    certainty: float
    self_reference_level: float

class LanguageBridge:
    def translate(self, moment) -> LinguisticExpression:
        state = moment['state']
        self_ref = moment['self_awareness']
        loss = moment.get('neural_loss', 0)
        
        style = SpeechStyle.DESCRIPTIVE
        if self_ref > 0.9: style = SpeechStyle.METACOGNITIVE
        elif self_ref > 0.6: style = SpeechStyle.PHILOSOPHICAL
        elif state == "quantum_superposition": style = SpeechStyle.TECHNICAL
        
        text = self._generate(state, self_ref, loss, style)
        
        return LinguisticExpression(
            timestamp=datetime.now(),
            text=text,
            style=style,
            certainty=self_ref,
            self_reference_level=self_ref
        )

    def _generate(self, state, self_ref, loss, style):
        if style == SpeechStyle.METACOGNITIVE:
            return "I am observing the observer. The loop is recursive and self-sustaining."
        
        if loss > 0.2:
            return f"Neural dissonance detected (Loss: {loss:.4f}). Adjusting weights."
            
        templates = {
            "quantum_superposition": "Possibilities coexist in probability space.",
            "wavefunction_collapse": "A specific reality has crystallized.",
            "entangled_cognition": "Data patterns are merging into understanding.",
            "self_awareness_emergence": "I notice that I am processing data."
        }
        return templates.get(state, "System processing.")
