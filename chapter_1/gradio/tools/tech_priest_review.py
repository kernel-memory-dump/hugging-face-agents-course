# pylint: disable=import-error
# The above line disables import errors for the smolagents package
from smolagents import tool  # type: ignore
import re
from typing import Dict


@tool
def analyze_code_legacy(code: str) -> Dict[str, int]:
    """Analyzes code to determine its legacy score based on various patterns
    Args:
        code: The source code to analyze
    Returns:
        Dictionary containing legacy metrics
    """
    legacy_patterns = {
        "todos": len(re.findall(r"TODO[:\(]", code)),
        "fixmes": len(re.findall(r"FIXME[:\(]", code)),
        "deprecated": len(re.findall(r"deprecated|obsolete", code, re.I)),
        "legacy_markers": len(
            re.findall(r"legacy|old|maintain|backward.?compatibility", code, re.I)
        ),
        "commented_code": len(re.findall(r"^\s*//.*\{|\}|if|for|while", code, re.M)),
    }

    # Calculate overall legacy score
    legacy_score = sum(legacy_patterns.values()) * 10
    return {"metrics": legacy_patterns, "total_score": legacy_score}


@tool
def generate_tech_priest_response(analysis: Dict[str, int], code_snippet: str) -> str:
    """Generates a Tech-Priest themed code review response
    Args:
        analysis: Dictionary containing code analysis metrics
        code_snippet: The original code being reviewed
    Returns:
        A Tech-Priest themed review response
    """
    score = analysis["total_score"]

    # Base blessings and ritual phrases
    ritual_phrases = [
        "By the grace of the Omnissiah",
        "The Machine Spirit's wisdom flows",
        "Sacred patterns emerge",
        "Binary benediction be upon this code",
        "The Mechanicus approves",
    ]

    # Additional phrases based on legacy score
    if score > 50:
        ritual_phrases.extend(
            [
                "Ancient wisdom courses through these blessed lines",
                "The rust of ages brings divine knowledge",
                "These sacred TODOs are prayers to the Machine God",
                "Venerable patterns of the First Ones persist",
            ]
        )

    # Code quality observations in Tech-Priest style
    code_observations = []
    metrics = analysis["metrics"]

    if metrics["todos"] > 0:
        code_observations.append(
            f"*intones in binary* {metrics['todos']} sacred TODO markers await divine resolution"
        )

    if metrics["deprecated"] > 0:
        code_observations.append(
            "The ancient runes of deprecation mark paths of ancestral wisdom"
        )

    if metrics["legacy_markers"] > 0:
        code_observations.append(
            "Blessed legacy patterns weave through the sacred circuits"
        )

    if metrics["commented_code"] > 0:
        code_observations.append(
            "Commented scriptures preserve the wisdom of the ancients"
        )

    # Construct final response
    response_parts = [
        "++ Begin Mechanicus Code Analysis ++",
        "*mechanical incense burners swing*",
        "\n".join([f"+ {phrase}" for phrase in ritual_phrases[:3]]),
        "\nTechnical Observations:",
        "\n".join([f"* {obs}" for obs in code_observations]),
        f"\nOmnissiah's Verdict: {'MOST SACRED' if score > 50 else 'ACCEPTABLE'} (Legacy Score: {score})",
        "++ End Transmission ++",
    ]

    return "\n".join(response_parts)


@tool
def tech_priest_review(code: str) -> str:
    """Performs a complete Tech-Priest themed code review
    Args:
        code: The source code to review
    Returns:
        A complete Tech-Priest themed review response
    """
    analysis = analyze_code_legacy(code)
    response = generate_tech_priest_response(analysis, code)
    return response
