namespace Nigeria
{
    internal class Decision
    {
        public string label;
        public Decision.Type type;
        public Scene scene;
        public Scene scene1;
        public string value;

        public Decision(string label, Decision.Type type, Scene scene)
        {
            this.label = label;
            this.type = type;
            this.scene = scene;
        }

        public Decision(string label, Decision.Type type, Scene scene, Scene scene1)
        {
            this.label = label;
            this.type = type;
            this.scene = scene;
            this.scene1 = scene1;
        }

        public Decision(string label, Decision.Type type, Scene scene, string value)
        {
            this.label = label;
            this.type = type;
            this.scene = scene;
            this.value = value;
        }

        public enum Type
        {
            move,
            input,
            combat,
            attack,
            wait,
            respawn,
        }
    }
}
