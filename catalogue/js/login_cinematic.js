/* Orchestration for Cinematic Login */

document.addEventListener('DOMContentLoaded', () => {
    const actor = document.querySelector('.actor-container');
    const plantStem = document.querySelector('.plant-stem');
    const seed = document.querySelector('.seed');
    const uiContainer = document.querySelector('.login-ui-container');

    // === TIMELINE ===

    // 0s: Start Walk
    setTimeout(() => {
        actor.classList.add('actor-walk');
    }, 100);

    // 2.5s: Stop & Bend
    setTimeout(() => {
        actor.classList.add('actor-bend');
    }, 2500);

    // 4s: Plant Seed
    setTimeout(() => {
        seed.classList.add('seed-drop');
        // Play minimal soil sound here in future
    }, 4000);

    // 5s: Grow Plant (Stem rises)
    setTimeout(() => {
        // Man stands back up
        actor.classList.remove('actor-bend');

        // Plant grows
        plantStem.classList.add('plant-grow');
        plantStem.classList.add('plant-leaves-grow');
    }, 5000);

    // 6.5s: Show UI (Mycelium network / organic pop)
    setTimeout(() => {
        uiContainer.classList.add('ui-visible');

        // Auto-focus username for UX
        const usernameInput = document.getElementById('id_username');
        if (usernameInput) usernameInput.focus();
    }, 6500);

});
