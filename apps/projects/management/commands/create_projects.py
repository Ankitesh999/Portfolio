from django.core.management.base import BaseCommand
from apps.projects.models import Project


class Command(BaseCommand):
    help = 'Create optimized projects with outcome-focused content'

    def handle(self, *args, **options):
        # Clear existing projects
        Project.objects.all().delete()
        
        # Research Paper Project
        research_paper = Project.objects.create(
            title="Applied ML Research (In Progress)",
            slug="applied-ml-research-in-progress",
            description="Investigating model behavior, experimental design, and generalization on real datasets.",
            content="""<p><strong>Research Focus:</strong> Applied ML research investigating model behavior and experimental design methodologies.</p>
            
            <h3>Why it matters:</h3>
            <p class="font-semibold text-blue-600">Focus on experimental rigor and understanding model generalization behavior.</p>
            
            <h3>Key Areas of Investigation</h3>
            <ul>
                <li>Model generalization on real-world datasets</li>
                <li>Experimental design for ML systems</li>
                <li>Evaluation rigor and reproducibility</li>
                <li>Data-centric AI approaches</li>
            </ul>
            
            <h3>Status</h3>
            <p><span class="bg-blue-100 text-blue-800 px-3 py-1 rounded-full text-sm font-semibold">Under Review (IEEE)</span> - Details to be disclosed post-review.</p>
            
            <h3>Impact</h3>
            <p>This research addresses critical gaps in ML model reliability and provides methodologies for robust, production-ready systems.</p>""",
            technologies="Machine Learning, Research, Experimental Design, Evaluation, Data Analysis",
            live_url="",
            github_url="",
            is_featured=True,
            order=1
        )
        
        # AI Advisor Platform
        ai_advisor = Project.objects.create(
            title="AI-Based Career Advisor Platform",
            slug="ai-based-career-advisor-platform",
            description="Personalized learning roadmaps using vector similarity and rule-based reasoning.",
            content="""<p><strong>Problem:</strong> Career guidance often relies on static templates rather than personalized, data-driven insights.</p>
            
            <h3>Why it matters:</h3>
            <p class="font-semibold text-green-600">Designed to reduce skill mismatch through data-driven recommendations.</p>
            
            <h3>Solution</h3>
            <p>Built an AI-driven system that generates personalized learning roadmaps and role recommendations based on individual skills and career goals.</p>
            
            <h3>Technical Implementation</h3>
            <ul>
                <li><strong>Feature Engineering:</strong> Vector representations for skills and career paths</li>
                <li><strong>Matching Algorithm:</strong> Cosine similarity for intelligent matching</li>
                <li><strong>Logic Layer:</strong> Rule-based reasoning for refined recommendations</li>
                <li><strong>Output:</strong> Structured learning roadmaps with milestone tracking</li>
            </ul>
            
            <h3>Key Features</h3>
            <ul>
                <li>Personalized career role recommendations</li>
                <li>Skill gap analysis and learning suggestions</li>
                <li>Data-driven insights vs static templates</li>
                <li>Interactive roadmap visualization</li>
            </ul>
            
            <h3>Technologies Used</h3>
            <p>Python for backend logic, Streamlit for frontend, ML algorithms for matching, and feature engineering techniques.</p>""",
            technologies="Python, Machine Learning, Streamlit, Feature Engineering, Cosine Similarity, Data Analysis",
            live_url="https://aiadvisor-project-ankitesh.streamlit.app/",
            github_url="",
            is_featured=True,
            order=2
        )
        
        self.stdout.write(
            self.style.SUCCESS('Successfully created projects with outcome focus!')
        )