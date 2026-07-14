from app.workflows.intelligence_workflow import IntelligenceWorkflow

def test_execute():
    workflow = IntelligenceWorkflow()
    assert workflow.execute() == "Enterprise intelligence workflow executed."
