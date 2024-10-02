document.getElementById('asset_category').addEventListener('change', function () {
    const assetTypeGroup = document.getElementById('asset_type_group');
    const buildingGroup = document.getElementById('building_group');
    const roomNumberGroup = document.getElementById('room_number_group');
    
    if (this.value === 'Employee Asset') {
        assetTypeGroup.style.display = 'none';
        buildingGroup.style.display = 'none';
        roomNumberGroup.style.display = 'none';
    } else if (this.value === 'Office Asset') {
        assetTypeGroup.style.display = 'block';
        buildingGroup.style.display = 'block';
        roomNumberGroup.style.display = 'block';
    }
});
