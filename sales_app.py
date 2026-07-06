import streamlit as st
from sales_engine import AISalesAutomationEngine

# High-end layout initialization
st.set_page_config(page_title="AI Sales Automation Suite", page_icon="📈", layout="wide")

# Modern clean typographical structure
st.title("AI Sales Automation & Financial Modeling Suite 📈")
st.caption("Next-generation data outreach hub running predictive operational ROI analytics.")
st.markdown("---")

# Left Column: Operational Controls | Right Column: Operator Metadata
col_ctrl1, col_ctrl2 = st.columns([2, 2])
with col_ctrl1:
    # UPDATED: Added "Education" to the market sector list
    industry_node = st.selectbox("🎯 SELECT TARGET MARKET SECTOR:", ["SaaS", "Healthcare", "Logistics", "Education"])
with col_ctrl2:
    rep_identity = st.text_input("🔑 OPERATOR SIGNATURE AUTHORITY:", value="Alex Sihag")

st.markdown("---")

if st.button("🚀 EXECUTE LIVE WORKFLOW PIPELINE SIMULATION", type="primary"):
    with st.spinner("Processing enterprise nodes and running financial matrices..."):
        
        # Instantiate backend infrastructure connection
        orchestrator = AISalesAutomationEngine(industry_node)
        active_pipeline = orchestrator.process_pipeline()
        
        st.markdown(f"### 📊 Active Node Telemetry (`Target Count: {len(active_pipeline)}`)")
        
        for node in active_pipeline:
            # 1. Compute high-tech algorithmic business simulations live
            metrics = orchestrator.calculate_predictive_roi(node["headcount"], node["avg_hourly_wage_usd"])
            proposal_code = orchestrator.craft_executive_brief(node, metrics, rep_identity)
            
            # 2. Render highly clean, standout visual grid containers
            with st.container(border=True):
                head_col1, head_col2 = st.columns([3, 1])
                with head_col1:
                    st.subheader(f"🏢 Enterprise Node: {node['name']}")
                    st.markdown(f"**Identified Bottleneck Vector:** `{node['bottleneck']}`")
                    st.caption(f"Current System Dependency: {node['incumbent']} | Headcount: {node['headcount']} FTEs")
                with head_col2:
                    st.write("")
                    st.status("Simulation Linked", state="complete")
                
                # Standout Metric Blocks for Financial Analytics
                st.markdown("#### ⚡ Real-Time Simulated ROI Indicators")
                met_col1, met_col2, met_col3 = st.columns(3)
                
                with met_col1:
                    st.metric(
                        label="Time Restored", 
                        value=f"{metrics['hours_recovered']:,} Hrs/mo", 
                        delta="🚀 +78% Efficiency"
                    )
                with met_col2:
                    st.metric(
                        label="Monthly Financial Recovery", 
                        value=f"${metrics['capital_saved_usd']:,} USD", 
                        delta="📉 Overhead Reduced"
                    )
                with met_col3:
                    st.metric(
                        label="Projected Annualized Savings", 
                        value=f"${(metrics['capital_saved_usd'] * 12):,} USD",
                        delta="🔥 High-Impact Return"
                    )
                
                # Visual performance loadbar indicator
                st.progress(0.78, text="System Optimization Potential Zone")
                
                st.markdown(" ")
                # Expandable code-block containing beautifully formatted data-driven script
                with st.expander("📄 EXTRACT COMPREHENSIVE OUTBOUND EXECUTIVE BRIEF"):
                    st.markdown("This outreach draft uses the precise financial metrics calculated above to capture executive attention:")
                    st.code(proposal_code.strip(), language="markdown")
else:
    # Beautiful minimalist empty layout state
    st.markdown("### 📡 Dashboard Ready")
    st.info("System currently uninitialized. Select your target market parameters above and trigger the pipeline execution to run the live ROI simulators.")