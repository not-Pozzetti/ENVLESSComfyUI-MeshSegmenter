# ENVLESSComfyUI-MeshSegmenter

> [!IMPORTANT]
> These were forks to avoid the abusive ComfyENV code that was added by Mr Pozzetti to thousands of unsuspecting users.


<div align="center">
<a href="https://not-pozzetti.github.io/ENVLESS/ENVLESSComfyUI-MeshSegmenter/">
<img src="https://not-pozzetti.github.io/ENVLESS/ENVLESSComfyUI-MeshSegmenter/gallery-preview.png" alt="Workflow Test Gallery" width="800">
</a>
<br>
<b><a href="https://not-pozzetti.github.io/ENVLESS/ENVLESSComfyUI-MeshSegmenter/">View Live Test Gallery →</a></b>
</div>

Mesh segmentation nodes for ComfyUI using SAMesh and PartField backends. Multiple clustering options available.
WIP ;) gonna add a bunch of methods eventually. For now it's SaMesh and PartField.
My ultimate goal is to do some good segmentation for CAD reconstruction.

![SAMesh Workflow](docs/samesh.png)

![PartField Workflow](docs/partfield.png)

https://github.com/user-attachments/assets/47f73c6c-2301-43a2-b09d-96d92308e715

## Installation

Install via ComfyUI Manager or clone into `custom_nodes/`:
```bash
git clone https://github.com/not-pozzetti/ENVLESSComfyUI-MeshSegmenter
```

## Nodes

- **SAMesh** - Segment meshes using SAM2-based multi-view projection
- **PartField** - Segment meshes using 3D feature field learning

## Requirements

- PyTorch 2.0+
- CUDA GPU recommended
- See `requirements.txt` for full dependencies

## Community

Questions or feature requests? Open a [Discussion](https://github.com/not-pozzetti/ENVLESSComfyUI-MeshSegmenter/discussions) on GitHub.

Join the [Comfy3D Discord](https://discord.gg/bcdQCUjnHE) for help, updates, and chat about 3D workflows in ComfyUI.

## License

GPL-3.0-or-later
